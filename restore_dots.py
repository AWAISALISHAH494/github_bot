import os
import subprocess
from datetime import datetime, timedelta
import random

# GitHub identity
GIT_AUTHOR_NAME = "Awais Khan"
GIT_AUTHOR_EMAIL = "awaisalishah02@gmail.com"  # Replace with your GitHub email

FILENAME = "log.txt"
DAYS_BACK = 365

# Initialize Git repo if needed
if not os.path.exists(".git"):
    subprocess.run(["git", "init"])
    subprocess.run(["git", "checkout", "-b", "main"])

# Create random commit activity for each day
for i in range(DAYS_BACK, 0, -1):
    commit_count = random.choice([0, 1, 2, 4, 6, 8, 10, 12])  # 0 = skip (no dot), 12 = darkest dot

    for j in range(commit_count):
        commit_time = datetime.now() - timedelta(days=i)
        commit_time_str = commit_time.strftime(f'%Y-%m-%d 12:{j:02d}:00')

        with open(FILENAME, 'a') as f:
            f.write(f"Commit {j+1} on {commit_time_str}\n")

        subprocess.run(["git", "add", FILENAME])
        subprocess.run([
            "git", "commit", "-m", f"Random commit {j+1} on {commit_time_str}",
            "--date", commit_time_str
        ], env={
            **os.environ,
            "GIT_AUTHOR_NAME": GIT_AUTHOR_NAME,
            "GIT_AUTHOR_EMAIL": GIT_AUTHOR_EMAIL,
            "GIT_COMMITTER_NAME": GIT_AUTHOR_NAME,
            "GIT_COMMITTER_EMAIL": GIT_AUTHOR_EMAIL
        })

print("\n✅ Updated restore_dots.py has created variable-color commits.")
print("👉 Run the following to push changes:\n")
print("   git push origin main --force")
