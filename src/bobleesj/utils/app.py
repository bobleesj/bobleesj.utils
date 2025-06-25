from argparse import ArgumentParser

from bobleesj.utils.cli.create import gif
from bobleesj.utils.cli.create import issues as create_issues
from bobleesj.utils.cli.delete import branch
from bobleesj.utils.cli.list import issues as list_issues




def setup_create_subcommands(subparsers):
    """
    Examples
    --------
    >>> bob create issues
    >>> bob create gif -p <path-to-the-video-file>
    """
    parser = subparsers.add_parser(
        "create", help="Create new issues, PRs, etc."
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True)
    commands = {
        "issues": ("Create issues.", create_issues.create),
        "gif": ("Create a GIF from a video file.", gif.create),
    }
    for name, (help_text, handler) in commands.items():
        subparser = subparsers.add_parser(name, help=help_text)
        if name == "gif":
            subparser.add_argument(
                "-p", "--path", required=True, help="Path to the video file"
            )
        subparser.set_defaults(func=handler)


def setup_delete_subcommands(subparsers):
    """
    Examples
    --------
    >>> bob delete local-branches
    """
    parser = subparsers.add_parser(
        "delete", help="Operations for deleting files, branches, etc."
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True)
    commands = {
        "local-branches": (
            "Delete all local branches.",
            branch.delete_local,
        ),
    }
    for name, (help_text, handler) in commands.items():
        subparser = subparsers.add_parser(name, help=help_text)
        subparser.set_defaults(func=handler)


def setup_list_subcommands(subparsers):
    """
    Examples
    --------
    >>> bob list issues
    """
    parser = subparsers.add_parser(
        "list", help="Operations for listing and viewing files."
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True)
    commands = {
        "issues": (
            "List all issues for each repository.",
            list_issues.list,
        ),
    }
    for name, (help_text, handler) in commands.items():
        subparser = subparsers.add_parser(name, help=help_text)
        subparser.set_defaults(func=handler)


def main():
    parser = ArgumentParser(
        description="Save time managing software packages."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    setup_test_subcommands(subparsers)
    setup_delete_subcommands(subparsers)
    setup_create_subcommands(subparsers)
    setup_list_subcommands(subparsers)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    """
    Examples:
    ---------
    >>> bob test package
    >>> bob test release
    >>> bob create issues
    >>> bob delete local-branches

    Not implemented:
    >>> bob test packages
    >>> bob delete local-branch
    >>> bob create issues
    """
    main()
