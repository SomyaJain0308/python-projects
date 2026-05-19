#!/usr/bin/env python3
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
IDLE_SECONDS = 5
POLL_INTERVAL = 1


def run_git(args):
    result = subprocess.run(
        ["git"] + args,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"git {' '.join(args)} failed with exit code {result.returncode}: {result.stderr.strip()}"
        )
    return result.stdout.strip()


def is_git_repo():
    return (REPO_ROOT / ".git").exists()


def get_branch_name():
    return run_git(["rev-parse", "--abbrev-ref", "HEAD"])


def has_changes():
    status = run_git(["status", "--porcelain"])
    return bool(status)


def stage_changes():
    run_git(["add", "-A"])


def commit_changes(branch):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Auto-save: {branch} @ {timestamp}"
    result = subprocess.run(
        ["git", "commit", "-m", message],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        if "nothing to commit" in result.stderr.lower():
            return False
        raise RuntimeError(
            f"git commit failed: {result.stderr.strip()}"
        )
    return True


def push_changes(branch):
    try:
        run_git(["rev-parse", "--abbrev-ref", "@{u}"])
        run_git(["push"])
    except RuntimeError:
        run_git(["push", "--set-upstream", "origin", branch])


def main():
    if not is_git_repo():
        print("Error: this script must be run from the repository root.")
        sys.exit(1)

    branch = get_branch_name()
    print(f"Auto Git watcher started in {REPO_ROOT}")
    print(f"Current branch: {branch}")
    print(f"Waiting for file changes. After 5s idle, changes will be staged, committed, and pushed.")

    dirty = False
    last_change = time.time()

    while True:
        try:
            if has_changes():
                if not dirty:
                    print("Changes detected. Waiting for idle period...")
                dirty = True
                last_change = time.time()
            elif dirty and time.time() - last_change >= IDLE_SECONDS:
                print("Idle period reached. Committing and pushing changes...")
                try:
                    stage_changes()
                    committed = commit_changes(branch)
                    if committed:
                        push_changes(branch)
                        print(f"Auto-pushed changes to {branch} at {datetime.now().strftime('%H:%M:%S')}.")
                    else:
                        print("No commit created because there were no staged changes.")
                except RuntimeError as exc:
                    print(f"Auto-push error: {exc}")
                dirty = False
            time.sleep(POLL_INTERVAL)
        except KeyboardInterrupt:
            print("\nAuto Git watcher stopped.")
            break
        except Exception as exc:
            print(f"Unexpected error: {exc}")
            time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
