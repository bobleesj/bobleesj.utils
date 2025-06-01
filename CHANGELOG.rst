=============
Release notes
=============

.. current developments

0.0.2
=====

**Added:**

* Add installation guide in the documentation.
* Check whether the elements from the formula is in the periodic table when ``Formula`` is initialized
* Implement ``Element.all_symbols()`` to return all 118 elements symbols from the periodic table.
* Implement ``radius.py`` module to get CIF and Pauling CN radius data for elements.
* Implement ``Elements`` enum for retrieving the name of the element given the symbol.
* Implement sorting of a formula by property, by index, and by defined custom labels.
* Implement parsing atomic mass, atomic number, element symbol and name with ``ptable.py`.


0.0.1
=====

**Added:**

* Create a new package with scikit-package.
* Implement Oliynyk database class for extracting data.
* Implement Formula class for parsing and working with chemical formula.
* Implement counting formulas to the ``Formula`` class.
* Add docstrings to ``Oliynyk``,  ``Property``, ``Formula`` classes.
* Add filter by composition, elements (containing/matching) in the Formula class.
* Add Jupyter Notebook support in the documentation.
