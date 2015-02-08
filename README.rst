Paper size related tools

This module provides tools to manipulate paper sizes, that is:

- a dictionary of several named standard names (e.g. A4, letter) , with their
  respective sizes (with and height);
- functions to convert sizes between units;
- functions to manipulate paper orientation (portrait or landscape);
- tools to parse paper sizes, so that you do not have to worry about the format
  of paper sizes provided by your user, it being `a4` or `21cm x 29.7cm`.

Install
=======

This module is compatible with both python 2 and 3.

* From sources::

    python setup.py install

* From pip::

    pip install papersize

Documentation
=============

You can build the documentation using::

  cd doc && make html