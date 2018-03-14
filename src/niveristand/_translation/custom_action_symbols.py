from niveristand._translation.py2rtseq import custom_generate_error
from niveristand._translation.py2rtseq import custom_localhost_wait
from niveristand._translation.py2rtseq import custom_math_log
from niveristand._translation.py2rtseq import custom_nivs_yield
from niveristand._translation.py2rtseq import custom_stop_task

"""Custom Action Symbols dictionary

Left-side: python symbol
Right-side: the function to call to process this symbol
"""
_custom_action_symbols = {
    'nivs_yield': custom_nivs_yield.custom_nivs_yield,
    'log': custom_math_log.custom_math_log,
    'localhost_wait': custom_localhost_wait.custom_localhost_wait,
    'stop_task': custom_stop_task.custom_stop_task,
    'generate_error': custom_generate_error.custom_generate_error,
}
