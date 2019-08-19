from collections import deque
from contextlib import contextmanager
from enum import Enum
import inspect
import logging
from threading import current_thread, Event, RLock, Thread
from niveristand import _errormessages, errors


def get_scheduler():
    return _Scheduler.get_scheduler()


@contextmanager
def multitask():
    """
    Creates a multitask context for branching execution.

    Refer to :func:`niveristand.library.multitask` for more details on branching execution.
    """
    multitask_info = _MultiTaskInfo()
    yield multitask_info
    # for a multitask the children need to be added to the queue ahead of the rest of the parent's tasks.
    # So here we reverse the list and add the tasks at the top because we don't know how far the bottom is.
    list.reverse(multitask_info.tasks)
    for task in multitask_info.tasks:
        get_scheduler().register_task_at_top(task)

    for task in multitask_info.tasks:
        task.start()

    this_task = get_scheduler().get_task_for_curr_thread()
    while not multitask_info.finished:
        if this_task.error and this_task.error.is_fatal:
            for task in multitask_info.tasks:
                task.stop_task()
        nivs_yield()
    if this_task.error and this_task.error.is_fatal:
        raise this_task.error


def nivs_yield():
    """
    Yields execution from this task or block to the next.

    Refer to :func:`niveristand.library.multitask` for more details on yielding to other tasks.
    """
    s = get_scheduler()
    task = s.thread_yielded()
    if not task.is_stopped():
        task.wait_for_turn()


class _MultiTaskInfo(object):
    task_id = 0

    def __init__(self):
        self.task = get_scheduler().get_task_for_curr_thread()
        self.tasks = []

    def add_func(self, func):
        task = _Task(func, parent=self, iteration_counter=self.task.iteration_counter)
        self.tasks.append(task)

    @property
    def finished(self):
        return all([t.is_stopped() for t in self.tasks])

    @classmethod
    def get_unique_task_name(cls):
        cls.task_id += 1
        return str(cls.task_id)


class _IterationCounter(object):
    def __init__(self):
        self._count = 0
        self._finished = False

    def inc(self):
        self._count += 1
        return self

    @property
    def count(self):
        return self._count

    @property
    def finished(self):
        return self._finished

    @finished.setter
    def finished(self, value):
        self._finished = value


class _Task(object):

    class _TaskState(Enum):
        Running = 0
        Stopping = 1
        Stopped = 2

    def __init__(self, func, parent=None, iteration_counter=None):
        if inspect.isfunction(func) or inspect.ismethod(func):
            self._task_name = func.__name__
            self._thread = Thread(
                target=func,
                args=(self,),
                name=self._task_name + '_' + _MultiTaskInfo.get_unique_task_name())
        else:
            self._thread = current_thread()
            self._task_name = str(func)
        self._state = _Task._TaskState.Running
        self._state_signal = Event()
        self._parent = parent
        self._generated_error = None
        self._iteration_counter = iteration_counter if iteration_counter else _IterationCounter()

    def start(self):
        self._thread.start()

    @property
    def parent(self):
        return self._parent

    @property
    def thread(self):
        return self._thread

    @property
    def iteration_counter(self):
        return self._iteration_counter

    def is_stopped(self):
        return self._state == _Task._TaskState.Stopped

    def is_stopping(self):
        return self._state == _Task._TaskState.Stopping

    def wait_for_turn(self):
        result = self._state_signal.wait()
        if self.is_stopping():
            self.mark_stopped()
            raise errors._StopTaskException
        return result

    def signal_to_run(self):
        self._state_signal.set()

    def move_to_ready(self):
        self._state_signal.clear()

    def mark_stopped(self):
        self._state = _Task._TaskState.Stopped

    def stop_task(self):
        # only mark a task as stopping if it's running, otherwise we could get into
        # an infinite loop of going between stopped and stopping.
        if self._state is _Task._TaskState.Running:
            self._state = _Task._TaskState.Stopping

    @property
    def error(self):
        return self._generated_error

    @error.setter
    def error(self, error):
        # cascade errors inside the previous reported error. Only the latest error is reported here, but all are
        # accessible traversing the chain.
        error.inner_error = self.error
        self._generated_error = error
        if self._parent:
            self._parent.task.error = error

    def __repr__(self):
        return "Task:name={} thread={}".format(self._task_name, str(self._thread))

    def __str__(self):
        return "Task:name={}".format(self._task_name)


class _Scheduler(object):
    _schedulers_lock = RLock()
    _scheduler = None

    @classmethod
    def get_scheduler(cls):
        with cls._schedulers_lock:
            if cls._scheduler is None:
                cls._scheduler = _Scheduler()
            return cls._scheduler

    def __init__(self):
        # a dictionary of {threadID:  _Task()}
        self._task_dict = dict()
        self._task_queue = deque()
        self._log = logging.getLogger('<sched>')
        self._last_sched = None

    @property
    def _can_sched(self):
        return not self._last_sched or self._last_sched is self.get_task_for_curr_thread()

    def sched(self):
        self._log.debug("Enter sched")
        # bail early if we were not waiting for this thread to yield
        if not self._can_sched:
            return False
        with self._schedulers_lock:
            try:
                # find the next task in the queue.
                next_task = self._task_queue.popleft()
                # if we have iteration counters, process them all.
                while isinstance(next_task, _IterationCounter):
                    next_task.inc()
                    # requeue the iteration counter only if it's not done counting
                    if not next_task.finished:
                        self._task_queue.append(next_task)
                    next_task = self._task_queue.popleft()

                # then tell it to run
                self._log.debug("Next task:%s", str(next_task))
                self._last_sched = next_task
                next_task.signal_to_run()
            except IndexError:
                # there was no work to do, so set the _last_sched to None
                self._last_sched = None
                return False
        return True

    def thread_yielded(self):
        task = self.get_task_for_curr_thread()
        self._log.debug("Task yielded:%s", str(task))
        # mark the yielding task ready to run
        task.move_to_ready()

        # if this thread is not finished, add it to the run queue
        if not task.is_stopped():
            self._log.debug("Reschedule Task :%s", str(task))
            self._task_queue.append(task)

        # then call sched() so the next thread is signaled to run if necessary
        self.sched()
        # finally, remove the task if it's not going to run anymore
        if task.is_stopped():
            self._log.debug("Finished Task :%s", str(task))
            # in case the task we're about to delete was the last one we were waiting for,
            # reset the last_sched marker.
            self.task_finished(task)
        return task

    def register_task_at_top(self, task):
        self._register_task_core(task, True)

    def register_task(self, task):
        self._register_task_core(task, False)

    def _register_task_core(self, task, at_top):
        self._task_dict[task.thread] = task
        self._log.debug("Register Task :%s", (str(task)))
        if at_top:
            self._task_queue.appendleft(task)
        else:
            self._task_queue.append(task)

    def task_finished(self, task):
        del self._task_dict[task.thread]

    def create_and_register_task_for_top_level(self):
        thread = current_thread()
        if thread in self._task_dict:
            raise errors.VeristandError(_errormessages.reregister_thread)
        task = _Task(thread.getName())
        # queue the task
        self.register_task(task)
        # queue an iteration counter for this top-level task
        self._task_queue.append(task.iteration_counter)
        return task

    def get_task_for_curr_thread(self):
        thread = current_thread()

        if thread not in self._task_dict:
            raise errors.VeristandError(_errormessages.unregistered_thread)
        return self._task_dict[thread]

    def try_get_task_for_curr_thread(self):
        try:
            task = self.get_task_for_curr_thread()
        except errors.VeristandError:
            task = None
        return task

    def get_task_by_name(self, taskname):
        found_tasks = [task for task in self._task_dict.values() if task._task_name == taskname]
        assert len(found_tasks) <= 1
        if found_tasks:
            return found_tasks[0]
        return None


def stop_task(task_function):
    """
    Stops the task you specify.

    Args:
        task_function:  task function you want to stop. You must have previously declared the task function inside
                        a :func:`multitask` context.


    Refer to :func:`niveristand.library.multitask` for more details on stopping tasks.

    """
    task = get_scheduler().get_task_by_name(task_function.__name__)
    if task:
        task.stop_task()
