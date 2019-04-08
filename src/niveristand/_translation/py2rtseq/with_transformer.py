import ast
from niveristand import _decorators, _errormessages, errors
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.library import _tasks


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
    validations.raise_if_try_in_node_body(node.body)
    if validations.check_if_any_in_block(ast.Return, node.body):
        raise errors.TranslateError(_errormessages.return_unsupported_unless_last)
    # this validation is the opposite of the usual funcdef check.
    # we must make sure ALL statements are ast.FunctionDef
    if any(not isinstance(stmt, ast.FunctionDef) for stmt in node.body):
        raise errors.TranslateError(_errormessages.return_unsupported_unless_last)
    if 'items' in dir(node):
        if len(node.items) > 1 or len(node.items) <= 0:
            raise errors.TranslateError(_errormessages.invalid_with_block)
        expr = node.items[0].context_expr
        opt_var = node.items[0].optional_vars
    else:
        expr = node.context_expr
        opt_var = node.optional_vars
    if not isinstance(expr, ast.Call):
        raise errors.TranslateError(_errormessages.invalid_with_block)
    # make sure the expression is "multitask()"
    func_name = _get_name_without_namespace_from_node(expr.func)
    if func_name is not _tasks.multitask.__name__ \
            or len(expr.args) > 0 \
            or opt_var is None:
        raise errors.TranslateError(_errormessages.invalid_with_block)
    return opt_var


def _validate_task(node, mt_name):
    body = node.body
    validations.raise_if_try_in_node_body(body)
    if validations.check_if_any_in_block(ast.FunctionDef, body):
        raise errors.TranslateError(_errormessages.invalid_function_definition)
    if validations.check_if_any_in_block(ast.Return, body):
        raise errors.TranslateError(_errormessages.return_unsupported_unless_last)
    if len(node.args.args) > 0:
        raise errors.TranslateError(_errormessages.invalid_with_block)
    decs = node.decorator_list
    if len(decs) != 1 \
            or not(isinstance(decs[0], ast.Call)) \
            or _get_name_without_namespace_from_node(decs[0].func) != _decorators.task.__name__ \
            or len(decs[0].args) != 1 \
            or decs[0].args[0].id is not mt_name.id:
        raise errors.TranslateError(_errormessages.invalid_with_block)
    return node


def _get_name_without_namespace_from_node(node):
    return utils.get_variable_name_from_node(node).split('.')[-1]
