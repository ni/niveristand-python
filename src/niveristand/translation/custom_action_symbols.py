from niveristand.translation.py2rtseq import custom_localhost_wait
from niveristand.translation.py2rtseq import custom_nivs_yield
from niveristand.translation.py2rtseq import custom_stop_task

"""Custom Action Symbols dictionary

Left-side: python symbol
Right-side: the function to call to process this symbol
"""
_custom_action_symbols = {
    'nivs_yield': custom_nivs_yield.custom_nivs_yield,
    'localhost_wait': custom_localhost_wait.custom_localhost_wait,
    'stop_task': custom_stop_task.custom_stop_task,
}
