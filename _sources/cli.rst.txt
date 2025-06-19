``bob <verb> <noun>`` commands
============================

Bob created useful CLI commands to increase productivity for developing and maintaining packages. These packages are created and maintained using ``scikit-package`` Level 5 ``public`` standard (https://scikit-package.github.io/scikit-package/).

Getting started
----------------

Create ``~/.bobrc`` with the following content:

    .. code-block:: bash

        {
            "dev_dir_path": "<path-to-your-folder-containing-packages>",
        }

``bob create <subcommand>``
---------------------------

Create issues in the GitHub repositories of the packages in the ``dev_dir_path`` specified in ``~/.bobrc``:

.. code-block:: bash

    $ bob create issues


Create a .gif from a video file:

.. code-block:: bash

    $ bob create gif -p <path-to-the-video-file>

``bob delete <subcommand>``
---------------------------

Delete all local branches except ``main``:

.. code-block:: bash

    $ bob delete local-branches

``bob test <subcommand>``
-------------------------

Create a new conda environment, install the dependencies from conda-forge, install the package in editable mode, and run the tests and pre-commit hooks. Ensure ``mamba`` is used.

.. code-block:: bash

    $ bob test package

.. note::

    It runs the following command internally:

    .. code-block:: bash

        mamba create -n {env_name} python=3.13 \\
        --file requirements/test.txt \\
        --file requirements/conda.txt \\
        --file requirements/docs.txt -y && \\
        source $(conda info --base)/etc/profile.d/conda.sh && \\
        mamba activate {env_name} && \\
        pip install --no-deps -e . && \\
        pip install pre-commit && \\
        pytest && pre-commit run --all-files


.. seealso::

    Do you have trouble running ``mamba``? Here is how you can download and install ``mamba`` if you don't have it installed yet. This version is for macOS:

    .. code-block:: bash

        $ rm -rf /Users/<macbook-username>/miniconda3
        $ rm -rf /Users/<macbook-username>/miniforge3
        $ curl -L -O "[https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$)(uname -m).sh"
        $ bash Miniforge3-$(uname)-$(uname -m).sh
        $ mamba shell init


Test whether the package can be uploaded to PyPI before releasing it:

.. code-block:: bash

    $ bob test release

.. note::

    It runs the following command internally:

    .. code-block:: bash

        mamba create -n {env_name} python=3.13 \\
        --file requirements/test.txt \\
        --file requirements/conda.txt \\
        --file requirements/docs.txt -y && \\
        source $(conda info --base)/etc/profile.d/conda.sh && \\
        mamba activate {env_name} && \\
        pip install build twine && \\
        pip install . --no-deps && \\
        python -m build && twine check dist/*
