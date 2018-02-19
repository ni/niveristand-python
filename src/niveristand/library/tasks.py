from contextlib import contextmanager


@contextmanager
def multitask():
    funcs = list()
    yield funcs
    for f in funcs:
        f()


def task(mt):
    def _add_task_to_list(func):
        mt.append(func)
        return func
    return _add_task_to_list


def nivs_yield():
    pass


def stop_task():
    pass
