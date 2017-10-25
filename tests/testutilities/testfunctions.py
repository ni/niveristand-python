from niveristand import decorators


@decorators.nivs_rt_sequence
def empty_func():
    pass

@decorators.nivs_rt_sequence
def simple_local_assignment():
    a = 5
