litecoin-python is a set of Python libraries that allows easy access to the
litecoin peer-to-peer cryptocurrency client API.

Documentation
===========================

Documentation can be found here, or in the source archive. It is built
using Sphinx:

http://deseret-tech.github.com/litecoin-python/doc/

Installation instructions
===========================

litecoin-python uses setuptools for the install script. There are no dependencies apart from Python itself.

::

  $ python setup.py build
  $ python setup.py install

Pypi / Cheeseshop
==================

It is possible to install the package through Pypi (cheeseshop), see http://pypi.python.org/pypi?:action=display&name=litecoin-python

::

  $ pip install litecoin-python

TODO
======
These things still have to be added:

- SSL support (including certificate verification) for managing remote litecoin daemons.

