===========  =================================================================================================================================
Info         NI VeriStand Python Support
Author       National Instruments
===========  =================================================================================================================================

.. _about_section:

About
=====
The **niveristand** package contains an API (Application Programming Interface)
for interacting with NI VeriStand systems. The package is implemented in Python.
This package was created and is supported by NI.

**niveristand** |version| supports the following versions of NI VeriStand:

- NI VeriStand 2017
- NI VeriStand 2018

The **niveristand** package requires installation of NI VeriStand on the system running the python code.

**niveristand** supports only the Windows operating system.

**niveristand** supports CPython 2.7 and 3.5+.

.. _installation_section:

Installation
============
Running **niveristand** requires NI VeriStand. Visit `ni.com/veristand <http://www.ni.com/veristand/>`_ for information on how to get the latest version of NI VeriStand.

**niveristand** can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install niveristand

Or **easy_install** from
`setuptools <http://pypi.python.org/pypi/setuptools>`_::

  $ python -m easy_install niveristand

You also can download the project source and run::

  $ python setup.py install


.. _usage_section:

Usage
=====
Refer to :doc:`basic_examples` for details on how to write a Python Real-Time Sequence.

.. _support_section:

Support / Feedback
==================

The **niveristand** package is supported by NI. For support for **niveristand**, open
a request through the NI support portal at `ni.com <http://www.ni.com>`_.

Bugs / Feature Requests
=======================

To report a bug or submit a feature request, please use the
`GitHub issues page <https://github.com/ni/niveristand-python/issues>`_.

Documentation
=============

Documentation is available `here <http://niveristand-python.readthedocs.io>`_.

Additional Documentation
========================
TODO: Get a real code for the VS docs!

Refer to the `NI VeriStand Help <http://digital.ni.com/express.nsf/bycode/exagg4>`_
for detailed information on setting up a system and running Real-Time test scenarios.

NI VeriStand Help installs only with the full version of NI VeriStand.

License
=======

**niveristand** is licensed under an MIT-style license (see `LICENSE
<LICENSE>`_).  Other incorporated projects may be licensed under different
licenses. All licenses allow for non-commercial and commercial use.
