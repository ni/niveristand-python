.. _getting_started_page:

===============
Getting Started
===============

Features
========

**niveristand** has two major capabilities: system definition and real-time sequence scripting. NI recommends you use an editor with code completion, such as `Visual Studio Code <https://code.visualstudio.com/docs/languages/python/>`_, to make it easier to browse and use this code.

Scripting system definition files
---------------------------------
You can script system definitions (.nivssdf) files for use in the NI VeriStand editor and deployable to the NI VeriStand engine.

Real-time sequences
-------------------
You can create and run NI VeriStand real-time (RT) sequences from Python that work in both the NI VeriStand engine and Stimulus Profile Editor:
- Convert Python functions into real-time sequences and save the converted Python functions to a file.
- Run test sequences in two different modes:

   - Deterministic Mode
      Deploys a real-time sequence to a running NI VeriStand system and executes the sequence in real-time.
   - Python Mode
      Runs a test sequence from a host machine that communicates with an NI VeriStand system through the Gateway.
      Python mode emulates the behavior of Deterministic mode. Python mode is useful in the following cases:

      - You need to debug your real-time sequence.
      - You want to take full advantage of the Python ecosystem.

.. include:: ../README.rst
   :start-after: _installation_section:
   :end-before: _usage_section:

Usage
=====
Refer to :doc:`sysdef_examples` for detailed examples of how to script a system definition file.

Refer to :doc:`basic_rt_sequence_examples` for detailed examples of how to write a Python real-time sequence.
