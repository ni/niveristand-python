.. _clientapi_examples:

===================
Client API Examples
===================

The Client API connects to a VeriStand Gateway to deploy systems, access channels,
monitor events, log data, and run stimulus profiles. Ensure the VeriStand Gateway
is running before using these examples.

Deploying a System Definition
=============================

Create a :any:`niveristand.clientapi.Factory`, obtain a workspace interface, and
connect the workspace to a system definition. Disconnect the system in a
``finally`` block so it is undeployed if an operation fails.

.. literalinclude:: ../examples/clientapi_example.py
   :language: python
   :pyobject: main
   :linenos:

Reading and Writing Channels
============================

Use the workspace to read and write scalar channel values.

.. literalinclude:: ../examples/clientapi_example.py
   :language: python
   :pyobject: use_channels
   :linenos:

Monitoring Channel Changes
==========================

Register a callback with a channel monitor to receive channel value change
events. Unregister the callback when monitoring is complete.

.. literalinclude:: ../examples/clientapi_example.py
   :language: python
   :pyobject: monitor_channel
   :linenos:

Monitoring Alarms
=================

Use the alarm manager to read alarm data and subscribe to alarm trigger events.

.. literalinclude:: ../examples/clientapi_example.py
   :language: python
   :pyobject: monitor_alarms
   :linenos:

Monitoring Model Parameters
===========================

Use the model manager to inspect model state and monitor changes to model
parameters.

.. literalinclude:: ../examples/clientapi_example.py
   :language: python
   :pyobject: monitor_models
   :linenos:

Logging Channel Data
====================

Create a TDMS logging specification, start a logging session, and stop the
session to retrieve the generated log files.

.. literalinclude:: ../examples/clientapi_example.py
   :language: python
   :pyobject: log_data
   :linenos:

Running a Stimulus Profile
==========================

Define a real-time sequence.

.. literalinclude:: ../examples/clientapi_example.py
   :language: python
   :pyobject: client_api_sequence
   :linenos:

Create and deploy a stimulus profile session, run its sequence, monitor the
completion event, and undeploy the session.

.. literalinclude:: ../examples/clientapi_example.py
   :language: python
   :pyobject: run_stimulus_profile
   :linenos: