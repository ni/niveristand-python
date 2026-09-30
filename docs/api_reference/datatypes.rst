.. _api_datatypes_page:

=======================
NI VeriStand Data types
=======================

.. autoclass:: niveristand.clientapi.BooleanValue
   :show-inheritance:

    Valid initialization values:

    * bool: True, False
    * string: 'true', 'false', 'True', 'False'
    * int, float: every valid value

    Examples:

    .. code-block:: python

        a = BooleanValue(True)
        a = BooleanValue(1.0)
        a = BooleanValue(1)


.. autoclass:: niveristand.clientapi.BooleanValueArray

    Valid initialization values:

    * a list of valid :class:`BooleanValue` initializers.

    Examples:

    .. code-block:: python

        a = BooleanValueArray([True, False])
        a = BooleanValueArray([1.0, 0.0])

.. autoclass:: niveristand.clientapi.ChannelReference
   :show-inheritance:

    Valid initialization values:

    * string: the path or alias for the channel.

    Examples:

    .. code-block:: python

        a = ChannelReference('Aliases/DesiredRPM')
        a = ChannelReference('Targets/Controller/Simulation Models/Models/Engine Demo/Inports/command_RPM')

.. autoclass:: niveristand.clientapi.DoubleValue
   :show-inheritance:

    Valid initialization values:

    * (int, float): all valid values.
    * bool: True (1.0), False (0.0)

   Non-float values are converted to their closest floating-point representation. Scientific notation is supported.

    Examples:

    .. code-block:: python

        a = DoubleValue(3.1415)
        a = DoubleValue(0xFFFF)
        a = DoubleValue(True)

.. autoclass:: niveristand.clientapi.DoubleValueArray

    Valid initialization values:

    * a list of valid :class:`DoubleValue` initializers.

    Examples:

    .. code-block:: python

        a = DoubleValueArray([1, 2.0, 0.3, 0x40])

.. autoclass:: niveristand.clientapi.I32Value
   :show-inheritance:

    Valid initialization values:

    * (int, float): [-2,147,483,648 to 2,147,483,647]
    * bool: True (1), False (0)

   Floating-point values are rounded down. Scientific notation is supported.

    Examples:

    .. code-block:: python

        a = I32Value(3)
        a = I32Value(3.1415)
        a = I32Value(0x7FFFFFFF)
        a = I32Value(True)
.. autoclass:: niveristand.clientapi.I32ValueArray

    Valid initialization values:

    * a list of valid :class:`I32Value` initializers.

    Examples:

    .. code-block:: python

        a = I32ValueArray([3, 3.1415, 0x7FFFFFFF, True])
.. autoclass:: niveristand.clientapi.I64Value
   :show-inheritance:

       Valid initialization values:

       * (int, float): [–9,223,372,036,854,775,808 to 9,223,372,036,854,775,807]
       * bool: True (1), False (0)

      Floating-point values are rounded down. Scientific notation is supported.

       Examples:

       .. code-block:: python

        a = I64Value(3)
        a = I64Value(3.1415)
        a = I64Value(0x7FFFFFFFFFFFFFFF)
        a = I64Value(-9.2e18)
        a = I64Value(True)
.. autoclass:: niveristand.clientapi.I64ValueArray

    Valid initialization values:

    * a list of valid :class:`I64Value` initializers.

    Examples:

    .. code-block:: python

        a = I64ValueArray([3, 3.1415, 0x7FFFFFFFFFFFFFFF, -9.2e18, True])

.. autoclass:: niveristand.clientapi.U32Value
   :show-inheritance:

       Valid initialization values:

       * (int, float): [0 to 4,294,967,295]
       * bool: True (1), False (0)

      Floating-point values are rounded down. Scientific notation is supported.

       Examples:

       .. code-block:: python

        a = U32Value(3)
        a = U32Value(3.1415)
        a = U32Value(0xFFFFFFFF)
        a = U32Value(True)

.. autoclass:: niveristand.clientapi.U32ValueArray

   Valid initialization values:

   * a list of valid :class:`U32Value` initializers.

   Examples:

   .. code-block:: python

      a = U32ValueArray([3, 3.1415, 0xFFFFFFFF, True])

.. autoclass:: niveristand.clientapi.U64Value
   :show-inheritance:

      Valid initialization values:

      * (int, float): [0 to 18,446,744,073,709,551,615]
      * bool: True (1), False (0)

      Floating-point values are rounded down. Scientific notation is supported.

      Examples:

      .. code-block:: python

         a = U64Value(3)
         a = U64Value(3.1415)
         a = U64Value(0x7FFFFFFFFFFFFFFF)
         a = U64Value(18.4e18)
         a = U64Value(True)

.. autoclass:: niveristand.clientapi.U64ValueArray

    Valid initialization values:

    * a list of valid :class:`U64Value` initializers.

    Examples:

    .. code-block:: python

        a = U64ValueArray([3, 3.1415, 0xFFFFFFFFFFFFFFFF, 18.4e18, True])
.. autoclass:: niveristand.clientapi.VectorChannelReference

    Valid initialization values:

    * string: path or alias for the channel.

    Examples:

    .. code-block:: python

        a = VectorChannelReference('engine/a')

.. autoclass:: niveristand.clientapi._datatypes.rtprimitives.DataType
