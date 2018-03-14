import ast
from niveristand._translation import utils


def augassign_transformer(node, resources):
    bin_op = ast.BinOp(node.target, node.op, node.value)
    assign_node = ast.Assign([node.target], bin_op)
    return utils.generic_ast_node_transform(assign_node, resources)
