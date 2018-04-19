.. _basic_examples:

====================
Basic Examples
====================

Writing a sequence
------------------
A Python real-time sequence is a Python function decorated with the :any:`niveristand.nivs_rt_sequence` decorator.
For example, the following sequence calls a function and checks the result.

.. literalinclude:: ../examples/basic_examples.py
   :language: python
   :linenos:
   :pyobject: call_add_two_numbers_test

The function also takes in some parameters. You must define parameters using the :any:`niveristand.NivsParam` decorator.

.. literalinclude:: ../examples/basic_examples.py
   :language: python
   :linenos:
   :pyobject: add_two_numbers

You can now run the test just like any other python function. You can run it non-deterministically, as in the following example:

.. literalinclude:: ../examples/basic_examples.py
   :language: python
   :linenos:
   :pyobject: run_add_two_numbers_tests
   :start-after: NON-Deterministic
   :end-before: DETERMINISTIC
   :emphasize-lines: 2

Or, you can run the test deterministically on the VeriStand engine connected to your system.

.. literalinclude:: ../examples/basic_examples.py
   :language: python
   :linenos:
   :pyobject: run_add_two_numbers_tests
   :start-after: DETERMINISTIC
   :emphasize-lines: 2

Combining the legacy API with real-time sequences
-------------------------------------------------

The :doc:`api_reference/legacy` can be mixed with python real-time sequences
to create a fully-automated test environment.

.. literalinclude:: ../examples/legacy_mix.py
   :language: python
   :linenos:

Array operations example
------------------------
.. literalinclude:: ../examples/basic_examples.py
   :language: python
   :linenos:
   :pyobject: array_operations


Measuring elapsed time example
------------------------------
.. literalinclude:: ../examples/basic_examples.py
   :language: python
   :linenos:
   :pyobject: measure_elapsed_time

State machine
-------------
.. literalinclude:: ../examples/basic_examples.py
   :language: python
   :linenos:
   :pyobject: state_machine_example
