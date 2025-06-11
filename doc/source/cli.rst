``bob <verb> <noun>`` commands
============================

Bob created useful CLI commands to increase productivity for developing and maintaining packages. These packages are created and maintained using ``scikit-package`` Level 5 ``public`` standard (https://scikit-package.github.io/scikit-package/).

How to get started
------------------

Create ``~/.bobrc`` with the following content:

    .. code-block:: bash

        {
            "packages": "<path-to-your-folder-containing-packages>",
        }

Manage GitHub repositories
--------------------------

#. Create many GitHub issues for all packages in the folder specified in ``~/.bobrc``:

    .. code-block:: bash
    
        $ bob create issues

#. Delete all local branches except ``main``:

    .. code-block:: bash

        $ bob delete local-branches

Manage packages locally
-----------------------

#. Build a new environment, install dependencies, run pytests, and pre-commit hooks:

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
            conda activate {env_name} && \\
            pip install --no-deps -e . && \\
            pip install pre-commit && \\
            pytest && pre-commit run --all-files

#. Test whether the package can be uploaded to PyPI before releasing it:

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
            conda activate {env_name} && \\
            pip install build twine && \\
            pip install . --no-deps && \\
            python -m build && twine check dist/*



 