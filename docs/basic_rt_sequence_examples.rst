.. _basic_rt_sequence_examples:

=================================
Basic Real-time Sequence Examples
=================================

Writing a real-time sequence
----------------------------
A Python real-time sequence is a Python function decorated with the :any:`niveristand.nivs_rt_sequence` decorator.
For example, the following sequence calls a function and checks the result.

.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: call_add_two_numbers_test

The function also takes in some parameters. You must define parameters using the :any:`niveristand.NivsParam` decorator.

.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: add_two_numbers

You can now run the test just like any other Python function. You can run it non-deterministically, as in the following example:

.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: run_add_two_numbers_tests
   :start-after: NON-Deterministic
   :end-before: DETERMINISTIC
   :emphasize-lines: 2

Or, you can run the test deterministically on the VeriStand engine connected to your system.

.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: run_add_two_numbers_tests
   :start-after: DETERMINISTIC
   :emphasize-lines: 2

Combining the legacy API with real-time sequences
-------------------------------------------------

To create a fully-automated test environment, you can mix the :doc:`api_reference/legacy` with Python real-time sequences.

.. literalinclude:: ../examples/legacy_mix.py
   :language: python
   :linenos:

Array operations example
------------------------
.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: array_operations


Measuring elapsed time example
------------------------------
.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: measure_elapsed_time

State machine
-------------
.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: state_machine_example
