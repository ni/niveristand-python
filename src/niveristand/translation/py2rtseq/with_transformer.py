import ast
from niveristand import decorators, errormessages, exceptions
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.library import tasks
from niveristand.translation import utils


def with_transformer(node, resources):
    mt_name = _validate_multitask(node)
    parent_block = resources.get_current_block()
    multi_task = rtseqapi.add_multi_task(parent_block)
    for task_def in [func_def for func_def in node.body if isinstance(func_def, ast.FunctionDef)]:
        _validate_task(task_def, mt_name)
        task_block = rtseqapi.add_task(multi_task, task_def.name)
        resources.set_current_block(task_block)
        for stmt in task_def.body:
            utils.generic_ast_node_transform(stmt, resources)
    resources.set_current_block(parent_block)


def _validate_multitask(node):
    if any(isinstance(stmt, ast.Return) for stmt in node.body):
        raise exceptions.TranslateError(errormessages.return_unsupported_unless_last)
    if any(not isinstance(stmt, ast.FunctionDef) for stmt in node.body):
        raise exceptions.TranslateError(errormessages.return_unsupported_unless_last)
    if 'items' in dir(node):
        if len(node.items) > 1 or len(node.items) <= 0:
            raise exceptions.TranslateError(errormessages.invalid_with_block)
        expr = node.items[0].context_expr
        opt_var = node.items[0].optional_vars
    else:
        expr = node.context_expr
        opt_var = node.optional_vars
    if not isinstance(expr, ast.Call):
        raise exceptions.TranslateError(errormessages.invalid_with_block)
    # make sure the expression is "multitask()"
    func_name = _get_name_without_namespace_from_node(expr.func)
    if func_name is not tasks.multitask.__name__ \
            or len(expr.args) > 0 \
            or opt_var is None:
        raise exceptions.TranslateError(errormessages.invalid_with_block)
    return opt_var


def _validate_task(node, mt_name):
    body = node.body
    if any(isinstance(stmt, ast.FunctionDef) for stmt in body):
        raise exceptions.TranslateError(errormessages.invalid_function_definition)
    if any(isinstance(stmt, ast.Return) for stmt in body):
        raise exceptions.TranslateError(errormessages.return_unsupported_unless_last)
    if len(node.args.args) > 0:
        raise exceptions.TranslateError(errormessages.invalid_with_block)
    decs = node.decorator_list
    if len(decs) is not 1 \
            or not(isinstance(decs[0], ast.Call)) \
            or _get_name_without_namespace_from_node(decs[0].func) != decorators.task.__name__ \
            or len(decs[0].args) is not 1 \
            or decs[0].args[0].id is not mt_name.id:
        raise exceptions.TranslateError(errormessages.invalid_with_block)
    return node


def _get_name_without_namespace_from_node(node):
    return utils.get_variable_name_from_node(node).split('.')[-1]
