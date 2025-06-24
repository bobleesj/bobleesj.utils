from pathlib import Path

def find_git_repos(root_dir):
    return [p.parent for p in Path(root_dir).rglob(".git")]
