from niveristand.clientapi import realtimesequencedefinition as rtseqapi


def create_rtseq_variable(variable_name, value, rt_seq):
    variable_name = rtseqapi.add_local_variable(rt_seq, variable_name, value)
    return variable_name


def add_assignment(block, dest_name, source_name):
    rtseqapi.add_assignment(block, dest_name, source_name)
