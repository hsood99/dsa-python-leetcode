# 🧩 Advanced Git Topics & Commands

This document covers important advanced Git concepts and commands to complement your Git learning. These topics are essential for mastering real-world Git workflows, troubleshooting, and collaboration.

---

## 1. git cherry-pick

- **Purpose:** Apply a specific commit from one branch onto another without merging the entire branch.

```bash
git checkout target-branch
git cherry-pick <commit-hash>
```

- **Use cases:** Backport bug fixes, apply specific commits selectively.

- **Handling conflicts:** Resolve conflicts manually, then:

```bash
git add <file>
git cherry-pick --continue
```

- **Abort cherry-pick:**

```bash
git cherry-pick --abort
```

---

## 2. git reflog

- **What is reflog?**  
  Git keeps a history of where HEAD and branches have pointed. This helps recover commits lost after resets, rebases, or accidental deletions.

- **View reflog:**

```bash
git reflog
```

- **Recover lost commit:**  
  Find commit hash in reflog, then:

```bash
git checkout <commit-hash>
# or to move branch back to that commit:
git reset --hard <commit-hash>
```

- **Common use:** Undo accidental resets, recover dangling commits.

---

## 3. Git Submodules

- **Definition:** A Git repository embedded inside another Git repository. Useful for including external projects as dependencies.

- **Add a submodule:**

```bash
git submodule add <repo-url> <path>
```

- **Clone a repo with submodules:**

```bash
git clone --recurse-submodules <repo-url>
```

- **Initialize and update submodules:**

```bash
git submodule update --init --recursive
```

- **Update submodules to latest commit on their branches:**

```bash
git submodule update --remote
```

- **Remove a submodule:**

1. Delete the entry from `.gitmodules` file.  
2. Run:

```bash
git rm --cached <submodule-path>
rm -rf <submodule-path>
```

---

## 4. git clean

- **Purpose:** Remove untracked files and directories to clean your working directory.

- **Preview files to be deleted (dry run):**

```bash
git clean -n
```

- **Remove untracked files:**

```bash
git clean -f
```

- **Remove untracked files and directories:**

```bash
git clean -fd
```

- **Warning:** This operation is irreversible. Use `-n` to preview first.

---

## 5. git reset vs git checkout vs git restore

| Command        | Purpose                                   | Common Use Case                                |
| -------------- | ----------------------------------------- | ---------------------------------------------- |
| `git reset`    | Move HEAD and adjust staging/index        | Undo commits, unstage files                    |
| `git checkout` | Switch branches or restore files (legacy) | Switch branches, restore file states           |
| `git restore`  | Restore files to a previous state (newer) | Discard local changes without switching branch |

- **Examples:**

```bash
git reset HEAD~1        # Undo last commit but keep changes staged
git restore file.txt    # Discard changes in file.txt
git checkout branch2    # Switch to branch2
```

---

## 6. Working with Multiple Remotes and Forks

- **Add additional remote (e.g., upstream original repo):**

```bash
git remote add upstream <original-repo-url>
```

- **Fetch and merge upstream changes:**

```bash
git fetch upstream
git merge upstream/main
```

- **Push changes to your fork:**

```bash
git push origin feature-branch
```

---

## 7. Branch Protection Rules (Advanced)

- Found in GitHub repository **Settings → Branches → Branch protection rules**
- Key features:
  - Require pull request before merging
  - Require status checks (e.g., CI tests)
  - Require reviews from code owners
  - Option to include administrators
- Helps enforce workflow discipline and prevent direct pushes to protected branches.
- When violated, pushing gives error:

```
! [remote rejected] main -> main (protected branch hook declined)
```

---

## 8. Pull Request (PR) Rules Enforcement and Bypass

- PRs must be created and approved to merge into protected branches.
- Admins can be given permission to bypass protection rules.
- To bypass temporarily, an admin can disable protection or merge via GitHub UI.

---

## 9. Commit Message Best Practices

Writing clear and meaningful commit messages is a crucial practice that improves collaboration, code history readability, debugging, and code reviews. Here's a complete guide tailored for both solo and team projects:

### ✅ Anatomy of a Good Commit Message

```
<type>(scope): Short, imperative summary (max ~50 characters)

Optional longer description or context if needed.
Explain *why* the change was made, not just *what* changed.

Refs: #IssueNumber (if applicable)
```

---

### ✍️ Golden Rules

| Rule | Why It Matters |
|------|----------------|
| ✅ Use imperative mood | E.g., "Fix bug", not "Fixed" or "Fixes" |
| ✅ Keep the summary line short | ~50 characters is ideal |
| ✅ Separate subject and body with a blank line | Improves clarity in logs |
| ✅ Use the body to explain why and how, not just what | Useful for future debugging or code archaeology |
| ✅ Reference issues/PRs if applicable | Links your changes to discussions |

---

### 🔧 Types of Commits (Conventional Commits)

| Type     | Use When You...                                |
|----------|------------------------------------------------|
| `feat`   | Add a new feature                              |
| `fix`    | Fix a bug                                      |
| `docs`   | Change documentation only                      |
| `style`  | Code style (formatting, whitespace, no logic)  |
| `refactor` | Refactor code without fixing or adding feature |
| `test`   | Add or update tests                            |
| `chore`  | Maintenance tasks (e.g., configs, package updates) |
| `ci`     | Update CI/CD-related code (e.g., GitHub Actions) |
| `perf`   | Improve performance                            |

---

### ✅ Good Commit Examples

```bash
feat(array): add sliding window max problem solution

Refactored previous implementation and added O(n) version.
Helps reduce time complexity for large datasets.
```

```bash
fix(auth): prevent login crash on null token

The issue was caused by unhandled null values in headers.
Added a default fallback and logging.
Refs: #124
```

```bash
docs(git): add cherry-pick explanation to notes.md
```

```bash
style: reformat array notes for consistent bullet usage
```

---

### ❌ Bad Commit Examples

| Bad Message     | Why It’s Bad                         |
|-----------------|--------------------------------------|
| `Update`        | Too vague — update what?             |
| `bug fixes`     | No explanation or scope              |
| `final changes` | Meaningless over time                |
| `done`          | Done what? Be specific               |
| `added file`    | What file? Why?                      |

---

### 💡 Pro Tips

- Use a linter like [`commitlint`](https://github.com/conventional-changelog/commitlint) to enforce message structure.
- Use `git commit -m "..."` for simple one-liners.
- For detailed commits, use `git commit` (without `-m`) to open a multi-line editor.
- Use `git log --oneline` to quickly review the readability of your history.

---

## 10. GitHub Notifications for Push Events

- Configure email notifications for pushes and PRs in GitHub repository  
  **Settings → Webhooks & Services → Notifications**
- Useful for CI/CD status alerts and team collaboration.

---

## 11. 🌱 Sparse Checkout

Sparse Checkout lets you check out only a subset of files or directories from a repository without cloning the entire working tree.

### ✅ Use Cases
- Working with monorepos
- Reducing disk usage and improving performance

### 🛠️ How to Use

```bash
# Clone normally
git clone https://github.com/user/repo.git
cd repo

# Enable sparse checkout
git sparse-checkout init

# Specify the folders to include
git sparse-checkout set path/to/folder1 path/to/folder2
```

To disable and restore full checkout:

```bash
git sparse-checkout disable
```

---

## 12. 🔄 Git Worktrees

Git Worktrees allow you to check out multiple branches at once in separate working directories.

```bash
git worktree add ../branch-folder-name branch-name
```

✅ **Use Cases**:
- Work on multiple features simultaneously
- Compare branches side-by-side

---

## 13. 🔍 Git Bisect

`git bisect` is a tool that helps identify the commit that introduced a bug by performing a binary search through the commit history.

### How It Works

You mark a known good commit and a known bad commit. Git then automatically checks out commits between these two points for testing. By marking each tested commit as good or bad, Git narrows down the commit that introduced the issue.

### Basic Workflow

1. Start bisecting:

    ```bash
    git bisect start
    ```

2. Mark the current commit as bad:

    ```bash
    git bisect bad
    ```

3. Mark a known good commit:

    ```bash
    git bisect good <commit-hash>
    ```

4. Test the checked out commit, then mark it as good or bad:

    ```bash
    git bisect good   # if the commit does not have the bug
    git bisect bad    # if the commit has the bug
    ```

5. Repeat steps 4 until Git finds the first bad commit.

6. End the bisect session:

    ```bash
    git bisect reset
    ```
---

# 📌 Summary

This document rounds out your Git mastery with important advanced commands and concepts. Use this as a reference for cherry-picks, reflog recovery, submodules, workspace cleaning, branch protections, and more.

*Happy Git mastering! 🚀*
