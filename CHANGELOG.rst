=============
Release notes
=============

.. current developments

0.0.4
=====


0.0.4
=====

**Added:**

* Implement functions to retrieve files with the specified file type and whether the folder contains the file extension.
* Add whether a list of elements are available for CIF/Pauling Radius.
* Implement bob create issues to generate issues across many repositories.
* Add bob <verb> <noun> CLI tutorials in the documentation.
* Implement bob delete local-branches to delete all branches except main.
* Add mendeleeve numbers under the sources module.


0.0.3
=====

**Added:**

* Implement ``bob test release`` so that the package check whether it can be released to PyPI after running ``twine check dist/*``.
* Implement ``bob test package`` to create a new environment to test the package fully.
* Support a total of 76 elements in the Oliynyk database with N, O, F, Cl, Br, I added.
* Implement ``bob update feedstock`` to prepare a PR to conda-forge feedstock with SHA256 and version updated from PyPI.
* Streamline news file creation process with ``bob add news -flag -m <news-message>`` entry point.


0.0.2
=====

**Added:**

* Add installation guide in the documentation.
* Check whether the elements from the formula is in the periodic table when ``Formula`` is initialized
* Implement ``Element.all_symbols()`` to return all 118 elements symbols from the periodic table.
* Implement ``radius.py`` module to get CIF and Pauling CN radius data for elements.
* Implement ``Elements`` enum for retrieving the name of the element given the symbol.
* Implement sorting of a formula by property, by index, and by defined custom labels.
* Implement parsing atomic mass, atomic number, element symbol and name with ``ptable.py``.


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
