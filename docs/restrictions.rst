.. _restrictions:

============
Restrictions
============

A collection of all restrictions inside a function using the :any:`nivs_rt_sequence` decorator. Any violation to these rules causes a :any:`TranslateError`.

Assignment
----------

- Value assignment to an already existing variable only works through the `value` property of the object.

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

- If statements only allow for bool checks. Numbers, numeric data type declarations or numeric variables are not allowed.

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

- Numeric constants and data type declarations are not allowed inside if expressions.

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

- Vector channel references will only work when running sequences deterministically.

- Only channel references can be initialized with strings. All other data type declarations will fail. Exception from this rule makes the BooleanValue which works for 'true', 'false', 'True' and 'False'.

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

- Generating an error is only allowed to have integer constants as error code, strings as error message and ErrorAction members as the error action.

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

- Passing down an NI VeriStand Data Type directly as a parameter of these functions is not allowed. As an alternative a variable or a data type declaration using the `value` property should be passed down.

    .. code-block:: python

        int_var = I32Value(-1)
        # Invalid usage
        int_var.value = abs(I32Value(-1))
        # Valid usages
        int_var.value = abs(I32Value(-1).value)
        int_var.value = abs(int_var.value)

- BooleanValue for `abs` behaves differently between Python and SPE.

    .. code-block:: python

        bool_var = BooleanValue(-5)
        bool_var.value = abs(bool_var.value)
        return bool_var.value # This is False in Stimulus Profile Editor, while True in Python.

Built-in VeriStand Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Some of these functions are not implemented in Python. Please refer to :any:`api_reference/library` for more information.

Function Definitions
--------------------

- It is not allowed to define new functions inside an if block, a loop or a task.

- `*args` and `kwargs` are not supported.

Loops
-----

- For loops do not support else blocks, ranges with start value, ranges with step value, ranges using a channel reference or constant arrays.

    .. code-block:: python

        # Invalid statements
        for x in range(5):
            pass
        else: # This is not allowed.
            pass
        for x in range(2, 5): # This is not allowed.
        for x in range(2, 5, 2): # This is not allowed.
        channel_ref = ChannelReference('Aliases/DesiredRPM')
        for x in range(channel_ref.value): # This is not allowed.
        for x in [1, 2, 3]: # This is not allowed.

- While loops do not support numeric constants as their condition, else blocks or break statements.

    .. code-block:: python

        # Invalid statements
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

- Several pluses one after another are not supported. Always use one.

    .. code-block:: python

        int_var = I32Value(0)
        int_var.value = 1 +++ 2 # This is not supported.
        int_var.value = 1 + 2 # Always use a single plus.

Arithmetic Shift
^^^^^^^^^^^^^^^^

- The left hand side of an arithmetic shift operation is not allowed to be of double type in Python.

    .. code-block:: python

        double_var = DoubleValue(5.0)
        # The following statements only work when the code is run deterministically
        double_var.value = DoubleValue(3.0) << 5
        double_var.value = 3.0 >> 5
        double_var.value = double_var.value >> 5

- The right hand side of an arithmetic shift operation is not allowed to be of double or bool type.

    .. code-block:: python

        bool_var = BooleanValue(True)
        bool_var.value = 5 >> BooleanValue(True)
        bool_var.value = 5 << True
        bool_var.value = 5 << bool_var.value
        double_var = DoubleValue(5.0)
        double_var.value = 5 >> DoubleValue(3.0)
        double_var.value = 5 << 3.0
        double_var.value = 5 << double_var.value

- The right hand side of an arithmetic shift operation is not allowed to be a negative number. As an alternative the opposite operation with positive value can be used.

    .. code-block:: python

        int_var = I32Value(1)
        int_var.value = int_var.value >> -2 # This is not allowed
        int_var.value = int_var.value << 2 # Use this instead

Bitwise Operators
^^^^^^^^^^^^^^^^^

- Bitwise operations are not allowed on floats or BooleanValue in Python.

    .. code-block:: python

        bool_var = BooleanValue(False)
        double_var = DoubleValue(1.0)
        # The following statements only work when the code is run deterministically
        bool_var.value = BooleanValue(True) & BooleanValue(True)
        double_var.value = 3.5 | 2.5
        double_var.value = DoubleValue(3.5) ^ DoubleValue(2.5)

Comparison Operators
^^^^^^^^^^^^^^^^^^^^

- Cascaded comparison operators are not allowed. Only use one at a time.

    .. code-block:: python

        int_var = I32Value(0)
        int_var.value = 1 == 2 == 3 == 4 # This is not allowed.

Logical Operators
^^^^^^^^^^^^^^^^^

- Logical operators only work with bool types.

- Cascaded logical operators are not allowed. Only use one at a time.

Unary Invert
^^^^^^^^^^^^

- The unary inversion operator (~) only works with integer types.

Parameters
----------

- Passing an immutable (such as the `value` property of an NI VeriStand Data Type) down as parameter by reference will not actually pass it by reference when the code is run in Python. This works well in the deterministic mode.

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
            return int_var.value # This will return 1 in Python, while 2 in SPE.

Return Statements
-----------------

- A function can only have a single return statement and it has to be the last line of the function.

- Return statements are not allowed inside an if block, a try block, a finally block, a loop, a multitask or a task.

- Only scalar values can be returned and the value has to be returned, not the object.

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

- Tasks with the same name are not allowed.

    .. code-block:: python

        with multitask() as mt:
            @task(mt)
            def f1():
                pass
            @task(mt)
            def f1(): # Task with the same name already exists.
                pass

- Multitasks and tasks are not allowed to have parameters.

    .. code-block:: python

        with multitask(param) as mt: # Parameter not allowed.
            @task(mt)
            def f1(param_task): # Parameter not allowed.

Try
---

- Try is only allowed to be the first statement of a function.

- It is not allowed to have a try inside another try, to be in an if block, else block, a loop, a task or a multitask.

- Try with except or orelse is not supported. Only the try-finally construct is supported.

Yield
-----

- It is not allowed to use yield as an operator or parameter.