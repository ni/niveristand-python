.. _basic_examples:

====================
Basic Examples
====================

Writing a sequence
------------------
A Python Real-Time Sequence is a Python function that has been decorated with the :any:`niveristand.nivs_rt_sequence` decorator.
For example, here we have sequence that will call a function and check the result.

.. literalinclude:: ../examples/basic_examples.py
   :language: python
   :linenos:
   :pyobject: call_add_two_numbers_test

The function that gets called also takes in some parameters.
Parameters need to be defined with the :any:`niveristand.NivsParam` decorator.

.. literalinclude:: ../examples/basic_examples.py
   :language: python
   :linenos:
   :pyobject: add_two_numbers

Finally, we can run our test either in a non-deterministic way just like any python function:

.. literalinclude:: ../examples/basic_examples.py
   :language: python
   :linenos:
   :pyobject: run_add_two_numbers_tests
   :start-after: NON-Deterministic
   :end-before: DETERMINISTIC
   :emphasize-lines: 2

Or run it deterministically on the VeriStand Engine our system is able to connect to.

.. literalinclude:: ../examples/basic_examples.py
   :language: python
   :linenos:
   :pyobject: run_add_two_numbers_tests
   :start-after: DETERMINISTIC
   :emphasize-lines: 2

Combining the legacy API with Real-Time sequences
-------------------------------------------------

The :doc:`api_reference/legacy` can be mixed with python Real-Time sequences
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
