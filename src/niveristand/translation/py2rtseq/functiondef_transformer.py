from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.internal import BLOCK, RTSEQ
from niveristand.translation import utils


def functiondef_transformer(node, resources):
    resources[RTSEQ] = rtseqapi.create_real_time_sequence()
    resources[BLOCK] = resources[RTSEQ].Code.Main.Body
    for instruction in node.body:
        utils.generic_ast_node_transform(instruction, resources)
    return ""
