# import os
from argparse import ArgumentParser
# from pathlib import Path

from bobleesj.utils.cli import conda_forge

#FIXME: Implmement hidden config file for scalability
BOB_CONFIG_FILE = "~/.bobrc"
# config_file = os.environ.get("BOB_CONFIG_FILE", BOB_CONFIG_FILE)
# config_file = Path(os.path.expandvars(config_file)).expanduser()
# exist_config = config_file.exists()
config = {
    "feedstock_path": "/Users/macbook/downloads/dev/feedstocks",
}


def update_feedstock():
    conda_forge.main(config)


def main():

    parser = ArgumentParser(
        description="Save time managing software packages."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # "update" command
    parser_update = subparsers.add_parser(
        "update", help="Update repositories and packages."
    )
    update_subparsers = parser_update.add_subparsers(
        dest="subcommand", required=True
    )

    # "feedstock" subcommand under "update"
    parser_feedstock = update_subparsers.add_parser(
        "feedstock",
        help="Prepare to create a PR to the conda-forge/main with updated "
        "version and SHA256 in meta.yaml.",
    )
    parser_feedstock.set_defaults(func=update_feedstock)

    args = parser.parse_args()
    args.func()


if __name__ == "__main__":
    main()
