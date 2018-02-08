from niveristand.translation.py2rtseq import custom_nivs_yield

"""Custom Action Symbols dictionary

Left-side: python symbol
Right-side: the function to call to process this symbol
"""
_custom_action_symbols = {

    'nivs_yield': custom_nivs_yield.custom_nivs_yield,
}
