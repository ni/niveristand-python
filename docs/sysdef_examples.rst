.. _sysdef_examples:

==========================
System Definition Examples
==========================

.. contents::
   :depth: 4

Basic Examples
==============

Creating a basic system definition file
---------------------------------------
A system definition can be created with a target operating system of Windows or Linux_x64.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: create_system_definition
   :linenos:
   :start-after: basename(filepath)
   :end-before: return

Be sure to save the system definition when you have made all necessary modifications.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: save_system_definition
   :linenos:
   :start-after: system definition."""


Adding User Channels, Calculated Channels, and Aliases
------------------------------------------------------
User channels can be added to a target.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_remaining
   :linenos:
   :start-after: # User Channel
   :end-before: # Procedure

Calculated channels can likewise be added to a target.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_remaining
   :linenos:
   :start-after: # Calculated Channel
   :end-before: # Alarm

Aliases get added to the system definition root instead of the target.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_remaining
   :linenos:
   :start-after: # Alias
   :end-before: # FPGA


Adding Alarms and Procedures
----------------------------
Procedures are added to a target.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_remaining
   :linenos:
   :start-after: # Procedure
   :end-before: # Calculated Channel

Alarms are also added to a target.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_remaining
   :linenos:
   :start-after: # Alarm
   :end-before: # Alias


Adding Models
-------------
Models are added to a target.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_models
   :linenos:
   :start-after: definition."""
   :end-before: sinewave_model


More Detailed Examples
======================

DAQ
---
There are many options available when adding DAQ devices.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_daq
   :linenos:
   :start-after: definition."""

CAN
---
An NI-XNET CAN interface can be added.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_can
   :linenos:
   :start-after: definition."""

LIN
---
An NI-XNET LIN interface can be added.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_lin
   :linenos:
   :start-after: definition."""

