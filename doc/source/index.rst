
#######
|title|
#######

.. |title| replace:: bobleesj.utils

``bobleesj.utils`` is a Python package for sharing utility functions and classes in materials informatics.

| Software version |release|
| Last updated |today|.

===============
Getting started
===============

- ``Formula`` to sort, filter, order formula(s).

- ``Oliynyk`` to parse Oliynyk elemental property database (https://doi.org/10.1016/j.dib.2024.110178).

- ``radius`` to parse available atomic radii for each element.

- ``Element`` to prevent typos in writing element symbols and names.

- ``ptable`` to parse the atomic number, atomic mass, element, and the name.

============
Installation
============

To install ``bobleesj.utils``, you can use pip or conda:

.. code-block:: bash

   $ pip install bobleesj.utils

If you prefer using ``conda``, you can install it from the conda-forge channel:

.. code-block:: bash

   $ conda install bobleesj.utils


=================
How to contribute
=================

Would you like to request new features? Please open issue on GitHub. Before you make a pull request, consider running ``pre-commit run --all-files`` to check the code style and formatting.

================
Acknowledgements
================

``bobleesj.utils`` is built and maintained with `scikit-package <https://scikit-package.github.io/scikit-package/>`_.

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: EXAMPLES

   notebooks/Formula
   notebooks/Oliynyk
   notebooks/radius
   notebooks/Element
   notebooks/ptable

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: COMMANDS

   cli

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: REFERENCE

   Package API <api/bobleesj.utils>
   release
   license
