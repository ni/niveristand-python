.. _getting_started_page:

===============
Getting Started
===============

Features
========

**niveristand** allows you to:

- Convert Python functions into NI VeriStand real-time (RT) sequences that are compatible with the NI VeriStand engine and Stimulus Profile Editor and save the converted Python functions to a file.
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
.. include:: ../README.rst
   :start-after: _usage_section:
   :end-before: _support_section:
