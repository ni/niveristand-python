import ast
import inspect
import tkinter
from tkinter import ttk
import testutilities.testfunctions


def pretty_print_ast(obj, graphical=False):
    node = ast.parse(inspect.getsource(obj))
    if graphical:
        AstGUIPrinter(node).print_all()
    else:
        AstPrinter(node).print_all()


class AstPrinter(object):
    def __init__(self, topnode):
        self.__indent = 0
        self._topnode = topnode

    def print_all(self):
        self.print_node(self._topnode)

    def print_node(self, node):
        self.print_with_indentation("%s(" % node.__class__.__name__)
        self.increment_indent()
        for field, value in ast.iter_fields(node):
            if isinstance(value, str) or isinstance(value, int):
                self.print_with_indentation("%s = '%s'" % (field, value))
            elif isinstance(value, list):
                self.print_with_indentation("%s = [" % field)
                self.increment_indent()
                for item in value:
                    self.print_node(item)
                self.decrement_indent("] # %s" % field)
            elif value is None:
                self.print_with_indentation("%s = None" % field)
            elif isinstance(value, ast.AST):
                self.print_with_indentation("%s =" % field)
                self.increment_indent()
                self.print_node(value)
                self.decrement_indent()
            else:
                raise Exception("Unexpected field type %s" % field)
        self.decrement_indent(") # %s" % node.__class__.__name__)

    def print_with_indentation(self, msg):
        print((' ' * self.__indent) + msg)

    def increment_indent(self):
        self.__indent += 4

    def decrement_indent(self, msg=None):
        self.__indent -= 4
        if msg is not None:
            self.print_with_indentation(msg)


class AstGUIPrinter(AstPrinter):
    def __init__(self, topnode):
        self._topwindow = tkinter.Tk()
        self._tree = ttk.Treeview(self._topwindow)
        self._curparent = ""
        self._prevparent = ""
        self._lastitem = ""
        super(AstGUIPrinter, self).__init__(topnode)

    def print_all(self):
        self.print_node(self._topnode)
        self._topwindow.geometry('300x900')
        self._tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
        self._topwindow.mainloop()

    def print_with_indentation(self, msg):
        self._lastitem = self._tree.insert(self._curparent, 'end', text=msg)

    def increment_indent(self):
        self._prevparent = self._curparent
        self._curparent = self._lastitem

    def decrement_indent(self, msg=None):
        self._curparent = self._prevparent
        self._prevparent = self._tree.parent(self._prevparent)


if __name__ == "__main__":
    pretty_print_ast(testutilities.testfunctions.simple_local_assignment, graphical=True)
