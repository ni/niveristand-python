init_var_invalid_type = "Variables must be initialized with a valid VeriStand datatype."
invalid_nested_funcdef = "Nested function definitions are only allowed inside a multitask."
invalid_top_level_func = "Invalid top level function."
save_without_valid_sequence = "No valid real-time sequence to save."
invalid_type_for_operator = "This operator doesn't support the given type."
name_constant_not_supported = "This named constant is not supported."
constant_not_supported = "This constant is not supported."
invalid_return_type = "Invalid return type."
invalid_return_value = "Return statement uses undeclared value."
invalid_type_to_convert = "Invalid conversion between types."
dependency_not_found = "Dependency not found."
invalid_type_for_channel_ref = "Channel references do not support the given type."
unsupported_orelse_while = "While loops do not support else blocks."
return_unsupported_unless_last = (
    "A function can only have a single return statement "
    "and it has to be the last line of the function."
)
break_unsupported = "Loops do not support break statements."
variable_reassignment = "Redefining a variable is not allowed."
cannot_change_array_elements = (
    "To assign values to an existing array element, "
    "you must use the value property of the object."
)
param_description_no_param = "The parameter specified in this definition does not exist."
invalid_function_definition = "Unsupported element in function definition."
invalid_param_decorator = "Parameter description decorator doesn't follow parameter rules."
unexpected_argument_redefine = "Unexpected argument added to list."
invalid_nivs_yield = "nivs_yield can only be used as a stand-alone statement."
invalid_with_block = "with statement can only be used inside multitask block."
for_else_not_supported = "for loops do not support else statements."
invalid_iterable_collection = "The iterable collection can only be a variable or a range(end)."
invalid_for_loop_iterator = "The iterator variable is not valid."
invalid_range_call = "range() can only be called with one parameter, the end value."
scalar_iterable_collection = "A for loop can only iterate on ArrayType."
invalid_stmt_after_try = "Invalid statement after try block. Only return statements are allowed."
try_must_be_first_stmt = "try must be the first statement in the function definition."
invalid_try_except_orelse = "try blocks do not support orelse or except blocks."
return_not_supported_in_try_finally = "return statement not supported inside a try/finally block."
try_only_in_top_level_func = (
    "The use of try is not allowed in this context. "
    "Use try/finally only as the first block in the top-level function."
)
invalid_taskname_for_stop_task = "The task name is invalid."
unregistered_thread = "Unregistered thread found."
reregister_thread = "Thread tried to register twice."
ref_param_not_ref = "A parameter marked as pass by reference was not of valid object type."
invalid_error_code_for_generate_error = (
    "Invalid error code provided. Provide an integer number as an error code."
)
invalid_message_for_generate_error = "Invalid error message provided. Provide a string message."
invalid_action_for_generate_error = (
    "Invalid error action provided. Provide an error action from ErrorAction enum."
)
unknown_identifier = "Undefined identifier '%s' found."
run_without_valid_sequence = "Invalid rtseq."
invalid_path_for_sequence = "Invalid real-time sequence path."
run_aborted = "The real-time sequence was stopped or aborted during run."
run_failed = "The real-time sequence failed."
csharp_call_failed = "The call into the C# API failed with error code %d. Message: %s."
channel_not_found = "A channel with name %s could not be found."
multiple_return_statements = "A function can only have a single return statement."
none_not_supported = "NoneType not supported."
invalid_decorator = "Custom decorators are not allowed."
cascaded_comparison_operators_not_allowed = (
    "You cannot use cascading comparison operators. " "Only use one comparison operator at a time."
)
invalid_operand_for_boolean_operator = "Logical operators only accept boolean values."
invalid_type_for_if_test = "If statements only allow for boolean checks."
invalid_operand_for_unary_invert_operator = (
    "The unary inversion operator (~) only accepts integer values."
)
negative_operand_for_binary_operator = (
    "You cannot use a negative number to the right of an arithmetic shift operation."
)
unexpected_dot_net_data_type = "Expecting a .net instance of type %s"
