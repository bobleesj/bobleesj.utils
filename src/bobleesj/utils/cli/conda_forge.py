from os.path import dirname, exists, join
import os
import click
import requests
from click import confirm, prompt
from bobleesj.utils.cli import auth
from bobleesj.utils.cli import api
from bobleesj.utils.cli.shell import run
from packaging.version import parse as parse_version


"""
This script streamlines the process of updating Python package versions and
their corresponding SHA256 hash in a meta.yaml file, followed by creating a
PR into the GitHub feedstock repository.

- The user is prompted to choose a feedstock directory
- The system prints the latest versions and SHA256 hashes from PyPI
- THe user confirms the version to udpate
- Fetch the user's GitHub username using the GitHub CLI for authentication
- Update the meta.yaml file with the new version and SHA256
- Commit these changes, pushes them to GitHub
- Create a PR from <username>/<version> to conda-forge/main
- Opens the web browser to review the PR
"""


def _update_meta_yaml(meta_file_path, new_version, new_sha256):
    """
    Update the meta.yaml file with the new version and SHA256 hash
    before making a PR to the feedstock repository.
    """
    with open(meta_file_path, "r") as file:
        lines = file.readlines()

    with open(meta_file_path, "w") as file:
        for line in lines:
            if "{%- set version =" in line:
                line = f'{{%- set version = "{new_version}" -%}}\n'
            elif "{% set version =" in line:
                line = f'{{% set version = "{new_version}" %}}\n'
            elif "sha256:" in line:
                line = f"  sha256: {new_sha256}\n"
            file.write(line)


def _run_gh_shell_command(
    cwd, meta_file_path, version, SHA256, username, pkg_name
):
    """
    Create a PR from a branch name of <new_version>
    to the main branch of the feedstock repository.
    """
    run("git stash", cwd=cwd) 
    run("git checkout main", cwd=cwd)
    run("git pull upstream main", cwd=cwd)
    # Create and switch to a new branch named after the new version
    run(f"git checkout -b {version}", cwd=cwd)
    # Update the meta.yaml file with the new version and SHA256
    _update_meta_yaml(meta_file_path, version, SHA256)
    # Add the updated meta.yaml file to the staging area
    run("git add recipe/meta.yaml", cwd=cwd)
    # Commit the changes
    run(f'git commit -m "release: update to {version}"', cwd=cwd)
    # Push the new branch to your origin repository
    run(f"git push origin {version}", cwd=cwd)
    run(
        f"gh repo set-default conda-forge/{pkg_name}-feedstock --branch {"main"}",
        cwd=cwd,
    )
    pr_command = (
        f"gh pr create --base main --head {username}:{version} "
        f"--title 'Update meta.yaml to {version}' "
        f"--body 'Updated meta.yaml to version {version} with SHA value of {SHA256}'"
    )
    # Run the PR create command in the appropriate directory
    run(pr_command, cwd=cwd)


def main():
    config = {
        "feedstock_path": "/Users/macbook/downloads/dev/feedstocks",
    }
    feedstock_path = config["feedstock_path"]
    feedstocks = [
        f for f in os.listdir(feedstock_path)
        if f.endswith("-feedstock") and os.path.isdir(os.path.join(feedstock_path, f))
    ]

    if not feedstocks:
        raise ValueError(
            f"No feedstocks found in {feedstock_path}. "
            "Please ensure you have cloned the feedstocks and set the correct path."
        )

    print("Available feedstocks:")
    version_map = {}
    for i, feedstock in enumerate(feedstocks, start=1):
        pkg_name = feedstock.replace("-feedstock", "")
        try:
            pkg_pypi_data = api.get_PyPI_version_SHA(pkg_name, count=1)
            pkg_version, pkg_sha256 = next(iter(pkg_pypi_data.items()))
            version_map[i] = {
                "package_name": pkg_name,
                "version": pkg_version,
                "sha256": pkg_sha256,
                "feedstock_dir_path": os.path.join(feedstock_path, feedstock),
                "meta_file_path": os.path.join(feedstock_path, feedstock, "recipe", "meta.yaml"),
            }
            print(f"  {i}. {pkg_name}, {pkg_version}, SHA256: {pkg_sha256[:5]}...")
        except ValueError:
            print(f"  {i}. {pkg_name}, [PyPI: Not Found]")


    choice = click.prompt(
        "Enter the number of the feedstock you want to update",
        type=click.IntRange(1, len(feedstocks))
    )
    selected = version_map[choice]
    username = auth.get_github_username()
    _run_gh_shell_command(
        selected["feedstock_dir_path"],
        selected["meta_file_path"],
        selected["version"],
        selected["sha256"],
        username,
        selected["package_name"]
    )
