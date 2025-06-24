import json
import subprocess
from datetime import datetime
from pathlib import Path

from bobleesj.utils.io import config, gh


def format_date(date_str):
    try:
        dt = datetime.fromisoformat(date_str.rstrip("Z"))
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return date_str


def format_labels(labels):
    if not labels:
        return "-"
    return ", ".join(label["name"] for label in labels)


def list_issues(repo_path):
    repo_name = Path(repo_path).name
    print(f"\n📁 Repository: {repo_name}")
    try:
        result = subprocess.run(
            [
                "gh",
                "issue",
                "list",
                "--state",
                "open",
                "--limit",
                "100",
                "--json",
                "number,title,createdAt,labels,author,milestone",
            ],
            cwd=repo_path,
            check=True,
            capture_output=True,
            text=True,
        )
        issues = json.loads(result.stdout)
        if not issues:
            print("No open issues.")
            return
        print(
            f"{'ID':<5} {'TITLE':<100} {'LABELS':<10} "
            f"{'AUTHOR':<15} {'MILESTONE':<20} {'CREATED'}"
        )
        print("-" * 175)
        for issue in issues:
            issue_id = str(issue["number"])
            title = issue["title"].strip().replace("\n", " ")
            created = format_date(issue["createdAt"])
            labels = format_labels(issue.get("labels", []))[:10]
            author = issue.get("author", {}).get("login", "unknown")
            milestone_data = issue.get("milestone")
            milestone = milestone_data["title"] if milestone_data else "-"
            print(
                f"{issue_id:<5} {title[:100]:<100} {labels:<10} "
                f"{author:<15} {milestone[:18]:<20} {created}"
            )

    except subprocess.CalledProcessError:
        print("❌ Failed to list issues.")


def list(args):
    root_dir = config.value("~/.bobrc", "dev_dir_path")
    if not root_dir or not Path(root_dir).is_dir():
        print(f"Error: '{root_dir}' is not a valid directory.")
        return
    repos = gh.find_git_repos(root_dir)
    if not repos:
        print("No Git repositories found.")
        return

    for repo in repos:
        list_issues(repo)
