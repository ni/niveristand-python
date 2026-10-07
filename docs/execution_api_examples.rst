.. _execution_api_examples:

======================
Execution API Examples
======================

These examples use :mod:`niveristand.clientapi` through a running VeriStand
Gateway. The examples below use the Engine Demo and Sinewave Delay system definition files for deployment.
Before running the examples below, ensure the system definition file path matches your VeriStand version.

Channel Access
==============

This example illustrates how to read, write and monitor channels.

.. literalinclude:: ../examples/channel_access.py
   :language: python
   :linenos:

Alarms
======

This example illustrates alarm monitoring. Runs the engine at high RPM in a warm environment to exceed the critical temperature limit continuously for the alarm's configured 30-second delay.

.. literalinclude:: ../examples/alarms.py
   :language: python
   :linenos:

Calibration
===========

This example applies polynomial calibration to a thermocouple channel in a DAQ.

.. literalinclude:: ../examples/calibration.py
   :language: python
   :linenos:

Channel Faulting
================

This example demonstrates how to set and clear channel faults.

.. literalinclude:: ../examples/channel_faulting.py
   :language: python
   :linenos:

Data Logging
============

This example demonstrates how to log channels to TDMS and text files.

.. literalinclude:: ../examples/data_logging.py
   :language: python
   :linenos:

Model Manager
=============

This example demonstrates how to read model execution state and signals, and monitor parameter changes.

.. literalinclude:: ../examples/model_manager.py
   :language: python
   :linenos:

Stimulus Profiles
=================

This example demonstrates how to deploy and run an existing real-time sequence using execution APIs.

.. literalinclude:: ../examples/stimulus_profile.py
   :language: python
   :linenos:

UDP Streaming
=============

This example shows how to deploy a UDP Stream Session to view buffered channel data published by the VeriStand Gateway. If any network errors occur, check your firewall settings for the specified UDP address and port.

.. literalinclude:: ../examples/udp_streaming.py
   :language: python
   :linenos:

Waveform Streaming
==================

This example shows how to start and register for waveform data published by the VeriStand Gateway.
Requirements: System Definition file containing waveforms and enter in a waveform path from that System Definition to view streaming in terminal.

.. literalinclude:: ../examples/waveform_streaming.py
   :language: python
   :linenos: