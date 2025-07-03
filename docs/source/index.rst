#######
|title|
#######

.. |title| replace:: bobleesj.utils

``bobleesj.utils`` is a Python package for sharing utility functions and classes in materials informatics.

|PyPI| |Forge| |PythonVersion|

|CI| |Codecov| |Tracking| |PR|

.. |CI| image:: https://github.com/bobleesj/bobleesj.utils/actions/workflows/matrix-and-codecov-on-merge-to-main.yml/badge.svg
        :target: https://github.com/bobleesj/bobleesj.utils/actions/workflows/matrix-and-codecov-on-merge-to-main.yml

.. |Codecov| image:: https://codecov.io/gh/bobleesj/bobleesj.utils/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/bobleesj/bobleesj.utils

.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/bobleesj.utils
        :target: https://anaconda.org/conda-forge/bobleesj.utils

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff
        :alt: GitHub pull requests
        :target: https://github.com/bobleesj/bobleesj.utils/pulls

.. |PyPI| image:: https://img.shields.io/pypi/v/bobleesj.utils
        :target: https://pypi.org/project/bobleesj.utils/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/bobleesj.utils
        :target: https://pypi.org/project/bobleesj.utils/

.. |Tracking| image:: https://img.shields.io/github/issues/bobleesj/bobleesj.utils
        :alt: GitHub issues
        :target: https://github.com/bobleesj/bobleesj.utils/issues

| Last updated |today|.

============
Installation
============

To install ``bobleesj.utils``, you can use pip or conda:

.. code-block:: bash

   $ pip install bobleesj.utils

If you prefer using ``conda``, you can install it from the conda-forge channel:

.. code-block:: bash

   $ conda install bobleesj.utils

===============
Getting started
===============

Classes:

- Use ``ElementSorter`` to sort elements in many way
- Use ``Formula`` to sort, filter, order formula(s).

Data sources:

- ``Oliynyk`` to work with the Oliynyk elemental property data.
- ``mendeleev`` to get the Mendeleev number for each element.
- ``radius`` to get the atomic radii for each element.
- ``Element`` to prevent typos in writing element symbols and names.
- ``ptable`` to parse the atomic number, atomic mass, element, and the name.
- ``folder`` to work with folders and files, used in CLI apps.


=========
Citations
=========

If you use the ``Oliynyk`` module in your research, please cite the  https://doi.org/10.1016/j.dib.2024.110178.

=================
How to contribute
=================

Would you like to request new features? Please open issue on GitHub. Before you make a pull request, consider running ``pre-commit run --all-files`` to check the code style and formatting.

============
Contributors
============

- Sangjoon Bob Lee (`@bobleesj <https://github.com/bobleesj>`_) - Maintainer
- Danila Shiryaev (`@dshirya <https://github.com/dshirya>`_) - Oliynyk elemental property data
- Anton Oliynyk (`@oliynyklab <https://github.com/oliynyklab>`_) - Oliynyk elemental property data
- Emil Jaffal (`@emiljaffal <https://github.com/emiljaffal>`_) - CIF radius interpolation

================
Acknowledgements
================

``bobleesj.utils`` is built and maintained with `scikit-package <https://scikit-package.github.io/scikit-package/>`_.

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: CLASSES

   notebooks/Formula
   notebooks/ElementSorter

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: DATA SOURCES

   notebooks/Oliynyk
   notebooks/radius
   notebooks/Element
   notebooks/ptable
   notebooks/mendeleev

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
