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

``bob list <subcommand>``
------------------------

#. List issues in the GitHub repositories of the packages in the ``dev_dir_path`` specified in ``~/.bobrc``:

    .. code-block:: bash

        $ bob list issues

``bob create <subcommand>``
---------------------------

#. Create issues in the GitHub repositories of the packages in the ``dev_dir_path`` specified in ``~/.bobrc``:

    .. code-block:: bash

        $ bob create issues

#. Create a .gif from a video file:

    .. code-block:: bash

        $ bob create gif -p <path-to-the-video-file>

``bob delete <subcommand>``
---------------------------

#. Delete all local branches except ``main``:

    .. code-block:: bash

        $ bob delete local-branches
