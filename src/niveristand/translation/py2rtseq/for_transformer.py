import ast

from niveristand import errormessages
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.clientapi.datatypes import ArrayType
from niveristand.exceptions import TranslateError
from niveristand.translation import utils
from niveristand.translation.py2rtseq import validations


def for_transformer(node, resources):
    _validate_restrictions(node)
    parent_block = resources.get_current_block()
    var_name = utils.get_variable_name_from_node(node.iter)
    if resources.has_variable(var_name):
        collection_value = resources.get_variable_py_value(var_name)
        if not isinstance(collection_value, ArrayType):
            raise TranslateError(errormessages.scalar_iterable_collection)
        collection = resources.get_variable_rtseq_name(var_name)
        iterator = node.target.id
        for_statement = rtseqapi.add_foreach_loop(parent_block, iterator, collection)
        # add the iterator as local variable, so that attribute_transformer returns the actual rtseq name of
        # the iterator
        resources.add_variable(iterator, 0, iterator)
        resources.add_variable(iterator + ".value", 0, iterator)
    elif utils.generic_ast_node_transform(node.iter, resources).startswith("range("):
        if len(node.iter.args) > 1:
            raise TranslateError(errormessages.invalid_range_call)
        max_range = utils.generic_ast_node_transform(node.iter.args[0], resources)
        variable = node.target.id
        for_statement = rtseqapi.add_for_loop(parent_block, variable, max_range)
    else:
        raise TranslateError(errormessages.invalid_iterable_collection)
    for statement in node.body:
        resources.set_current_block(for_statement.Body)
        utils.generic_ast_node_transform(statement, resources)
    resources.set_current_block(parent_block)


def _validate_restrictions(node):
    if node.orelse:
        raise TranslateError(errormessages.for_else_not_supported)
    if not isinstance(node.iter, (ast.Name, ast.Attribute, ast.Call)):
        raise TranslateError(errormessages.invalid_iterable_collection)
    if not isinstance(node.target, ast.Name):
        raise TranslateError(errormessages.invalid_for_loop_iterator)
    validations.check_try_in_node_body(node.body)
