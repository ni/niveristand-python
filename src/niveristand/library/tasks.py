from contextlib import contextmanager


@contextmanager
def multitask():
    funcs = list()
    yield funcs
    for f in funcs:
        f()


def nivs_yield():
    pass
