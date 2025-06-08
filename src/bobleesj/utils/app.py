# import os
    
from argparse import ArgumentParser
from bobleesj.utils.cli import test

def main():
    parser = ArgumentParser(
        description="Save time managing software packages."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- Test command ---
    test_parser = subparsers.add_parser(
        "test", help="Test the package with a new conda environment."
    )
    test_subparsers = test_parser.add_subparsers(dest="subcommand", required=True)
    test_commands = [
        ("package", "Test the single package.", test.build_pytest),
        ("release", "Test the release condition for the package.", test.build_check_release)
    ]
    for name, help_text, handler in test_commands:
        subparser = test_subparsers.add_parser(name, help=help_text)
        subparser.set_defaults(func=handler)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    """
    Examples:
    ---------
    >>> bob test package
    >>> bob test packages (not implemented)
    >>> bob delete local-branch (not implemented)
    >>> bob create issues (not implemented)
    >>> bob test release
    
    """
    main()
