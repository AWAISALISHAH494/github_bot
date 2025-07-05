import os
import subprocess
from datetime import datetime, timedelta
import random

# GitHub Identity
GIT_AUTHOR_NAME = "Awais Khan"
GIT_AUTHOR_EMAIL = "awaisalishah02@gmail.com"  # <-- Replace this

FILENAME = "log.txt"
DAYS_BACK = 365

# Make sure we are in a git repo
if not os.path.exists(".git"):
    subprocess.run(["git", "init"])
    subprocess.run(["git", "checkout", "-b", "main"])

# Loop through each past day
for i in range(DAYS_BACK, 0, -1):
    commit_count = random.choice([0, 1, 2, 4, 6, 8, 12])  # Varying commits/day

    for j in range(commit_count):
        date = datetime.now() - timedelta(days=i)
        commit_time = date.replace(hour=12, minute=j % 60)
        commit_time_str = commit_time.strftime('%Y-%m-%d %H:%M:%S')

        # Write unique content per commit
        with open(FILENAME, 'a') as f:
            f.write(f"{commit_time_str} - Commit #{j + 1} on day {i}\n")

        subprocess.run(["git", "add", FILENAME])
        subprocess.run([
            "git", "commit", "-m", f"Unique commit {j+1} on {commit_time_str}",
            "--date", commit_time_str
        ], env={
            **os.environ,
            "GIT_AUTHOR_NAME": GIT_AUTHOR_NAME,
            "GIT_AUTHOR_EMAIL": GIT_AUTHOR_EMAIL,
            "GIT_COMMITTER_NAME": GIT_AUTHOR_NAME,
            "GIT_COMMITTER_EMAIL": GIT_AUTHOR_EMAIL
        })

print("\n✅ All commits made. Now push them forcefully:")
print("   git push origin main --force")
