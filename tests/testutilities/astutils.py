import ast
import astdump
import inspect
import testutilities.testfunctions

def pretty_print_ast(obj):
    src = inspect.getsource(obj)
    astdump.indented(src)


if __name__ == "__main__":
    pretty_print_ast(testutilities.testfunctions)