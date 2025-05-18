# 🧩 Advanced Git Topics & Commands

This document covers important advanced Git concepts and commands to complement your Git learning. These topics are essential for mastering real-world Git workflows, troubleshooting, and collaboration.

---

## 1. git cherry-pick

- **Purpose:** Apply a specific commit from one branch onto another without merging the entire branch.
- **Usage:**

  ```bash
  git checkout target-branch
  git cherry-pick <commit-hash>
````

* **Use cases:**
  Backport bug fixes, apply specific commits selectively.

* **Handling conflicts:**
  Resolve conflicts manually, then:

  ```bash
  git add <file>
  git cherry-pick --continue
  ```

* **Abort cherry-pick:**

  ```bash
  git cherry-pick --abort
  ```

---

## 2. git reflog

* **What is reflog?**
  Git keeps a history of where HEAD and branches have pointed. This helps recover commits lost after resets, rebases, or accidental deletions.

* **View reflog:**

  ```bash
  git reflog
  ```

* **Recover lost commit:**
  Find commit hash in reflog, then:

  ```bash
  git checkout <commit-hash>
  # or to move branch back to that commit:
  git reset --hard <commit-hash>
  ```

* **Common use:** Undo accidental resets, recover dangling commits.

---

## 3. Git Submodules

* **Definition:** A Git repository embedded inside another Git repository. Useful for including external projects as dependencies.

* **Add a submodule:**

  ```bash
  git submodule add <repo-url> <path>
  ```

* **Clone a repo with submodules:**

  ```bash
  git clone --recurse-submodules <repo-url>
  ```

* **Initialize and update submodules:**

  ```bash
  git submodule update --init --recursive
  ```

* **Update submodules to latest commit on their branches:**

  ```bash
  git submodule update --remote
  ```

* **Remove a submodule:**

  1. Delete the entry from `.gitmodules` file.
  2. Run:

  ```bash
  git rm --cached <submodule-path>
  rm -rf <submodule-path>
  ```

---

## 4. git clean

* **Purpose:** Remove untracked files and directories to clean your working directory.

* **Preview files to be deleted (dry run):**

  ```bash
  git clean -n
  ```

* **Remove untracked files:**

  ```bash
  git clean -f
  ```

* **Remove untracked files and directories:**

  ```bash
  git clean -fd
  ```

* **Warning:** This operation is irreversible. Use `-n` to preview first.

---

## 5. git reset vs git checkout vs git restore

| Command        | Purpose                                   | Common Use Case                                |
| -------------- | ----------------------------------------- | ---------------------------------------------- |
| `git reset`    | Move HEAD and adjust staging/index        | Undo commits, unstage files                    |
| `git checkout` | Switch branches or restore files (legacy) | Switch branches, restore file states           |
| `git restore`  | Restore files to a previous state (newer) | Discard local changes without switching branch |

* **Examples:**

  ```bash
  git reset HEAD~1        # Undo last commit but keep changes staged
  git restore file.txt    # Discard changes in file.txt
  git checkout branch2    # Switch to branch2
  ```

---

## 6. Working with Multiple Remotes and Forks

* **Add additional remote (e.g., upstream original repo):**

  ```bash
  git remote add upstream <original-repo-url>
  ```

* **Fetch and merge upstream changes:**

  ```bash
  git fetch upstream
  git merge upstream/main
  ```

* **Push changes to your fork:**

  ```bash
  git push origin feature-branch
  ```

---

## 7. Branch Protection Rules (Advanced)

* Found in GitHub repository **Settings → Branches → Branch protection rules**.
* Key features:

  * Require pull request before merging.
  * Require status checks (e.g., CI tests).
  * Require reviews from code owners.
  * Include administrators option to allow/disallow bypass.
* Helps enforce workflow discipline and prevent direct pushes to protected branches.
* When violated, pushing gives error:

  ```
  ! [remote rejected] main -> main (protected branch hook declined)
  ```

---

## 8. Pull Request (PR) Rules Enforcement and Bypass

* PRs must be created and approved to merge into protected branches.
* Admins can be given permission to bypass protection rules.
* To bypass temporarily, an admin can disable protection or merge via GitHub UI.

---

## 9. Commit Message Best Practices

* Use clear, concise messages.

* Follow format:

  ```
  type(scope): short description
  ```

* Examples:

  ```
  feat(parser): add support for new syntax
  fix(ui): fix button alignment issue
  docs(readme): update installation instructions
  ```

* Use imperative mood (e.g., "Add", not "Added" or "Adding").

* Reference related issue or PR if applicable.

---

## 10. GitHub Notifications for Push Events

* Configure email notifications for pushes and PRs in GitHub repository **Settings → Webhooks & Services → Notifications**.
* Useful for CI/CD status alerts and team collaboration.

---

# Summary

This document rounds out your Git mastery with important advanced commands and concepts. Use this as a reference for cherry-picks, reflog recovery, submodules, workspace cleaning, branch protections, and more.

*Happy Git mastering! 🚀*
