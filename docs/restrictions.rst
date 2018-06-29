.. _restrictions:

============
Restrictions
============

The following section contains a list of all restrictions inside a function using the :any:`nivs_rt_sequence` decorator. If you violate any of the following rules, a :any:`TranslateError` occurs.

Assignment
----------

- To assign values to an existing variable, you must use the `value` property of the object.

    .. code-block:: python

        int_var = I32Value(0)
        int_array_var = I32ValueArray([1, 2, 3])
        # Invalid value assignments
        int_var = 5
        int_array_var = [2, 3, 4]
        int_array_var[2] = 5
        # Valid value assignments
        int_var.value = 5
        int_array_var.value = [2, 3, 4]
        int_array_var[2].value = 5

- Redefining a variable is not allowed.

    .. code-block:: python

        int_var = I32Value(0)
        int_var = DoubleValue(1.0) # The variable is already defined.

Conditional
-----------

- `If` statements only allow for boolean checks. You cannot use numbers, numeric data type declarations, or numeric variables inside `If` statements.

    .. code-block:: python

        # Invalid conditions
        int_var = I32Value(0)
        if 1:
        if I32Value(0):
        if int_var.value:
        # Valid conditions
        bool_var = BooleanValue(True)
        if True:
        if False:
        if BooleanValue(True):
        if bool_var.value

- You cannot use numeric constants or data type declarations inside `If` expressions.

    .. code-block:: python

        # Invalid conditions
        int_var = I32Value(0)
        int_var.value = 1 if 1 else 2
        int_var.value = 1 if DoubleValue(1) else 2
        int_var.value = 1 if int_var.value else 2
        # Valid conditions
        bool_var = BooleanValue(True)
        int_var.value = 1 if True else 2
        int_var.value = 1 if BooleanValue(True) else 2
        int_var.value = 1 if bool_var.value else 2

Data Types
----------

- Vector channel references will only work when you run sequences deterministically.

- Channel references are the only data type declarations you can initialize with strings. All other data type declarations will fail.
    * Note: The BooleanValue data type is an exception to this rule. You can initialize BooleanValue with 'true' 'false' 'True' and 'False'.

    .. code-block:: python

        # Invalid variable declarations
        bool_var = BooleanValue("string")
        double_var = DoubleValue("3.0")
        int32_var = I32Value("1")
        int64_var = I64Value("1")
        uint32_var = U32Value("1")
        uint64_var = U64Value("1")
        bool_array_var = BooleanValueArray([True, "False"])
        double_array_var = DoubleValueArray([3.0, 5.0, "6.0"])
        int32_array_var = I32ValueArray([1, 2, "3"])
        int64_array_var = I64ValueArray([1, 2, "3"])
        uint32_array_var = U32ValueArray([1, 2, "3"])
        uint64_array_var = U64ValueArray([1, 2, "3"])

- Signed integers cannot use the full range of values.

    .. code-block:: python

        int32_invalid_var = I32Value(0xFFFFFFFF)
        int32_last_valid_var = I32Value(0x7FFFFFFF)
        int64_invalid_var = I64Value(0xFFFFFFFFFFFFFFFF)
        int64_last_valid_var = I64Value(0x7FFFFFFFFFFFFFFF)

Error Generation
----------------

-  When you generate an error, you can only use integer constants for the error code parameter, strings for the error message parameter, and ErrorAction members as the error action parameter.

    .. code-block:: python

        # Valid statement
        generate_error(-1, "My error", ErrorAction.AbortSequence)
        # Invalid statements
        int_var = I32Value(-1)
        generate_error(int_var.value, "My error", ErrorAction.AbortSequence)
        generate_error(-1, 2, ErrorAction.AbortSequence)
        generate_error(-1, "My error", 3)

Functions
---------

Built-in Math Functions
^^^^^^^^^^^^^^^^^^^^^^^

- You cannot pass down an NI VeriStand data type directly as a parameter of the built-in math functions. As an alternative, you can pass a variable or data type declaration to these functions using the `value` property.

    .. code-block:: python

        int_var = I32Value(-1)
        # Invalid usage
        int_var.value = abs(I32Value(-1))
        # Valid usages
        int_var.value = abs(I32Value(-1).value)
        int_var.value = abs(int_var.value)

- BooleanValue for `abs` behaves differently between Python and Stimulus Profile Editor.

    .. code-block:: python

        bool_var = BooleanValue(-5)
        bool_var.value = abs(bool_var.value)
        return bool_var.value # This returns False in the Stimulus Profile Editor but returns True in Python.

Built-in VeriStand Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Some of these functions are not implemented in Python. Please refer to :any:`api_reference/library` for more information.

Function Definitions
--------------------

- You cannot define new functions inside an `if` block, a loop, or a task.

- The `*args` and `kwargs` variables are not supported.

Loops
-----

- `For Loops` do not support:
    * `else` blocks
    * ranges with a start value
    * ranges with a step value
    * ranges that use a channel reference
    * ranges that use array constants

    .. code-block:: python

        # The following statements are invalid:
        for x in range(5):
            pass
        else:
            pass
        for x in range(2, 5):
        for x in range(2, 5, 2):
        channel_ref = ChannelReference('Aliases/DesiredRPM')
        for x in range(channel_ref.value):
        for x in [1, 2, 3]:

- `While Loops` do not support:
    * using `else` blocks
    * using a numeric constant as the condition
    * using `break` statements

    .. code-block:: python

        # The following statements are invalid:
        int_var = I32Value(5)
        while 1:
        while int_var:
        while int_var.value:
        while True:
            pass
        else:
            pass
        while True:
            break

Operators
---------

Add
^^^

- You cannot use several pluses one after another. Always use one plus sign. If you violate this rule, a :any:`TranslateError` occurs.

    .. code-block:: python

        int_var = I32Value(0)
        int_var.value = 1 +++ 2 # This is not supported.
        int_var.value = 1 + 2 # Always use a single plus.

Arithmetic Shift
^^^^^^^^^^^^^^^^

- You cannot use double data types to the left of an arithmetic shift operation in Python.

    .. code-block:: python

        double_var = DoubleValue(5.0)
        # The following statements only work when the code is run deterministically.
        double_var.value = DoubleValue(3.0) << 5
        double_var.value = 3.0 >> 5
        double_var.value = double_var.value >> 5

- You cannot use double or boolean data types to the right of an arithmetic shift operation.

    .. code-block:: python

        bool_var = BooleanValue(True)
        bool_var.value = 5 >> BooleanValue(True)
        bool_var.value = 5 << True
        bool_var.value = 5 << bool_var.value
        double_var = DoubleValue(5.0)
        double_var.value = 5 >> DoubleValue(3.0)
        double_var.value = 5 << 3.0
        double_var.value = 5 << double_var.value

- You cannot use a negative number to the right of an arithmetic shift operation. As an alternative, use the opposite operation with a positive value.

    .. code-block:: python

        int_var = I32Value(1)
        int_var.value = int_var.value >> -2 # This is not allowed.
        int_var.value = int_var.value << 2 # Use this instead.

Bitwise Operators
^^^^^^^^^^^^^^^^^

- You cannot use bitwise operations on float or boolean values in Python.

    .. code-block:: python

        bool_var = BooleanValue(False)
        double_var = DoubleValue(1.0)
        # The following statements only work when the code is run deterministically.
        bool_var.value = BooleanValue(True) & BooleanValue(True)
        double_var.value = 3.5 | 2.5
        double_var.value = DoubleValue(3.5) ^ DoubleValue(2.5)

Comparison Operators
^^^^^^^^^^^^^^^^^^^^

- You cannot use cascading comparison operators. Only use one comparison operator at a time.

    .. code-block:: python

        int_var = I32Value(0)
        int_var.value = 1 == 2 == 3 == 4 # This is not allowed.

Logical Operators
^^^^^^^^^^^^^^^^^

- Logical operators only accept boolean values.

- You cannot use cascading logical operators. Only use one logical operator at a time.

Unary Invert
^^^^^^^^^^^^

- The unary inversion operator (~) only accepts integer values.

Parameters
----------

- If you need to pass an immutable object (such as the `value` property of an NI VeriStand data type) by reference, you must run your code deterministically. Otherwise, the parameter will not actually pass by reference when you run the code in Python.

    .. code-block:: python

        @NivsParam('param', DoubleValue(0), NivsParam.BY_REF)
        @nivs_rt_sequence
        def _increment_by_ref(param):
            param.value += 1
            return param.value


        @nivs_rt_sequence
        def call_increment_by_ref():
            int_var = I32Value(1)
            _increment_by_ref(int_var.value)
            return int_var.value # This will return 1 in Python and 2 in the Stimulus Profile Editor.

Return Statements
-----------------

- A function can only have a single return statement and it has to be the last line of the function.

- You cannot use return statements inside an `if` block, a `try` block, a `finally` block, a loop, a multitask, or a task.

- Return statements can only return scalar values through the `value` property.

    .. code-block:: python

        int_var = I32Value(1)
        int_array_var = I32ValueArray([1, 2, 3])
        # Invalid return statements
        return int_var
        return int_array_var
        return DoubleValueArray[1.0, 2.0]
        # Valid return statements
        return int_var.value
        return int_array_var[0].value

Tasks
-----

- You cannot create more than one task with the same name.

    .. code-block:: python

        with multitask() as mt:
            @task(mt)
            def f1():
                pass
            @task(mt)
            def f1(): # Task with the same name already exists.
                pass

- You cannot create parameters for tasks or multitasks.

    .. code-block:: python

        with multitask(param) as mt: # Parameter not allowed.
            @task(mt)
            def f1(param_task): # Parameter not allowed.

Try
---

- `Try` is only allowed to be the first statement of a function.

- You cannot use a `try` statement within:
    * another `try` statement
    * an `if` block
    * an `else` block
    * a loop
    * a task
    * a multitask

- You cannot use a `try` statement with `except` or `orelse`.

Yield
-----

- You cannot use `yield` as an operator or parameter.