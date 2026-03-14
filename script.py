import os
import random
import subprocess
from datetime import datetime, timedelta

FILE = "info.txt"

def run(cmd, env=None):
    subprocess.run(cmd, check=True, env=env)

def commit_with_date(message, date):
    env = os.environ.copy()
    git_date = date.strftime("%Y-%m-%dT12:00:00")

    env["GIT_AUTHOR_DATE"] = git_date
    env["GIT_COMMITTER_DATE"] = git_date

    run(["git", "add", FILE])
    run(["git", "commit", "-m", message, "--date", git_date], env=env)

def fake_commits(start_date, end_date, min_commits, max_commits):

    current_date = start_date

    while current_date <= end_date:

        commits_today = random.randint(min_commits, max_commits)

        print(f"{commits_today} commits on {current_date.date()}")

        for i in range(commits_today):

            content = f"{current_date} commit {i} {random.random()}"

            with open(FILE, "a") as f:
                f.write(content + "\n")

            commit_with_date(content, current_date)

        current_date += timedelta(days=1)

    print("Pushing commits...")
    run(["git", "push"])


start = datetime(2026,1,1)
end = datetime(2026,3,14)

fake_commits(start, end, 1, 10)