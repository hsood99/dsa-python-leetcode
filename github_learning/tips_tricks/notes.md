# 📌 Git Tips & Tricks

This document consolidates useful Git commands, tips, and best practices to improve your daily workflow and avoid common pitfalls.

---

## 🔹 Aliases for Faster Commands

Create shortcuts for frequently used commands:

```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
````

Example:
`git co main` instead of `git checkout main`.

---

## 🔹 Undoing Commits and Changes

* Undo last commit but keep changes staged:

  ```bash
  git reset --soft HEAD~1
  ```

* Amend last commit (modify message or add staged changes):

  ```bash
  git commit --amend
  ```

* Discard changes in working directory (unstage):

  ```bash
  git checkout -- <file>
  ```

* Unstage staged files:

  ```bash
  git reset HEAD <file>
  ```

---

## 🔹 Stashing Work In-Progress

Temporarily save uncommitted changes:

```bash
git stash
git stash list
git stash apply
git stash pop
```

Useful when switching branches without committing partial work.

---

## 🔹 Cleaning Untracked Files

Remove files not tracked by Git:

```bash
git clean -f       # Remove untracked files
git clean -fd      # Remove untracked files and directories
git clean -n       # Dry run (preview removal)
```

---

## 🔹 Visualizing Commit History

* Show compact commit graph:

  ```bash
  git log --oneline --graph --decorate --all
  ```

* Custom readable log format:

  ```bash
  git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short
  ```

---

## 🔹 Partial Commits (Add Patches Interactively)

Stage specific parts of files:

```bash
git add -p
```

You’ll be prompted to review and select hunks.

---

## 🔹 Pull with Rebase

Avoid unnecessary merge commits when syncing with remote:

```bash
git pull --rebase
```

Set globally:

```bash
git config --global pull.rebase true
```

---

## 🔹 Rebase and Squash Commits

Clean history before pushing:

```bash
git rebase -i HEAD~n   # Replace n with number of commits
```

Squashing combines commits for a cleaner history.

---

## 🔹 Reset vs Revert

* `git reset` rewrites history by moving branch pointer (dangerous on shared branches).

* `git revert` safely undoes changes by creating a new commit.

---

## 🔹 Checking Differences

* Between working directory and last commit:

  ```bash
  git diff
  ```

* Between staged changes and last commit:

  ```bash
  git diff --cached
  ```

* Between two branches or commits:

  ```bash
  git diff branch1..branch2
  ```

---

## 🔹 Useful Git Configurations

* Enable color in output:

  ```bash
  git config --global color.ui auto
  ```

* Set preferred editor (example: VS Code):

  ```bash
  git config --global core.editor "code --wait"
  ```

---

## 🔹 Git Reflog

`git reflog` lets you see all changes to HEAD, even ones lost from normal logs — useful to recover lost commits:

```bash
git reflog
```

You can then reset to any previous state from reflog:

```bash
git reset --hard <reflog-hash>
```

---

## 🔹 Git Submodules

Submodules allow embedding external repos within your repo:

* Add submodule:

  ```bash
  git submodule add <repo-url> path/to/submodule
  git commit -m "Add submodule"
  ```

* Clone repo with submodules:

  ```bash
  git clone --recurse-submodules <repo-url>
  ```

* Update submodules after cloning:

  ```bash
  git submodule update --init --recursive
  ```

---

## 🔹 Viewing Branch Tracking Info

To check which remote branch a local branch is tracking:

```bash
git branch -vv
```

---

## 🔹 Checking File History

See all commits touching a file:

```bash
git log --follow -- <file>
```

---

## 🔹 Clean Up Local Branches

Delete merged local branches safely:

```bash
git branch --merged
git branch -d branch_name
```

Delete unmerged branches (force delete):

```bash
git branch -D branch_name
```

---

## 🔹 Git Garbage Collection

Clean up unnecessary files and optimize repo:

```bash
git gc
```

---

## 📌 Summary

Implementing these tips helps you:

* Speed up your workflow
* Maintain a cleaner commit history
* Handle mistakes effectively
* Collaborate better with others

Happy Git hacking! 🚀

```


