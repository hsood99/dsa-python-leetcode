# Git Basics — Comprehensive Notes

Welcome to the **Git Basics** section! This document consolidates everything discussed so far and serves as your one-stop resource to master Git fundamentals and professional workflows. By the end of this, you'll understand Git commands, branching strategies, PR enforcement, personal access tokens, repo structure, commit lifecycle, and much more.

---

## 📦 Table of Contents

1. [Git Installation & Setup](#git-installation--setup)
2. [Initial Configuration](#initial-configuration)
3. [Create & Initialize a Git Repository](#create--initialize-a-git-repository)
4. [Core Git Commands](#core-git-commands)
5. [Branching in Git](#branching-in-git)
6. [Merging & Pull Requests](#merging--pull-requests)
7. [Protecting Branches & PR Rules](#protecting-branches--pr-rules)
8. [Forking & Collaboration](#forking--collaboration)
9. [Personal Access Tokens (PAT)](#personal-access-tokens-pat)
10. [Setting Up .gitignore](#setting-up-gitignore)
11. [Working with VS Code + Git](#working-with-vs-code--git)
12. [GitHub Actions Workflow](#github-actions-workflow)
13. [Useful Flags & Options](#useful-flags--options)

---

## 1. Git Installation & Setup

* ✅ Official Git site: [https://git-scm.com/downloads](https://git-scm.com/downloads) (Safe)
* Choose first SSL option: "Use OpenSSL library" — more compatible with Linux/macOS.
* Git works well across all OSes — Windows, Linux, macOS.

## 2. Initial Configuration

For a new machine or new Git user:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"
```

## 3. Create & Initialize a Git Repository

```bash
mkdir my-repo
cd my-repo
git init
```

Or clone an existing one:

```bash
git clone https://github.com/your-username/your-repo.git
```

## 4. Core Git Commands

```bash
git status        # View current state
git add .         # Stage all changes
git commit -m "message"  # Commit staged changes
git push origin branch-name  # Push to remote
git pull origin branch-name  # Pull from remote
```

### Common Warning

```bash
warning: LF will be replaced by CRLF...
```

Don't worry, it’s just line-ending conversion on Windows.

---

## 5. Branching in Git

```bash
git branch feature/my-feature     # Create branch
git checkout feature/my-feature   # Switch to it
# OR in one step:
git checkout -b feature/my-feature
```

### Deleting Branches

```bash
git branch -d branch-name              # Local delete
git push origin --delete branch-name  # Remote delete
```

* `-d` is short for `--delete`
* `--` is a flag separator to avoid ambiguity

---

## 6. Merging & Pull Requests

### Local Merge:

```bash
git checkout main
git merge feature/my-feature
```

### Remote PR:

1. Push your branch:

```bash
git push origin feature/my-feature
```

2. Raise PR from `feature/my-feature` → `main` on GitHub
3. After merge, delete branch from UI or:

```bash
git branch -d feature/my-feature
git push origin --delete feature/my-feature
```

---

## 7. Protecting Branches & PR Rules

* Go to GitHub → Settings → Branches → Add protection rule for `main`
* Enforce:

  * PR before merging
  * Include administrators ✅
  * Dismiss stale reviews / require approvals

🔒 This prevents direct push to main. You'll see:

```bash
remote: Changes must be made through a pull request.
```

---

## 8. Forking & Collaboration

* You can’t fork your own repo, but you can:

  * Clone it
  * Create branches
  * Work via PRs

For other accounts:

```bash
git clone https://github.com/username/repo.git
```

---

## 9. Personal Access Tokens (PAT)

* GitHub → Settings → Developer Settings → PATs → Generate new token
* Use it in place of password when pushing via HTTPS

---

## 10. Setting Up .gitignore

Use `.gitignore` to exclude files:

```
__pycache__/
*.pyc
.env
.DS_Store
```

---

## 11. Working with VS Code + Git

* VS Code automatically detects Git repo.
* Git tab shows uncommitted changes.
* Stage, commit, and push directly from the UI.
* If changes are not appearing:

  * Ensure files are tracked
  * Check `.gitignore`

---

## 12. GitHub Actions Workflow

Create file at:

```
.github/workflows/python-test.yml
```

### Example:

```yaml
name: Python Tests
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
    steps:
    - uses: actions/checkout@v2
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: pytest
```

---

## 13. Useful Flags & Options

* `--delete` vs `-d`: Same effect (short vs long form)
* `--`: Separates flags from positional args

---

## ✅ Summary Workflow for Any New Change

1. Create a new branch
2. Make changes and commit locally
3. Push the branch to origin
4. Raise a PR to `main`
5. Merge PR
6. Delete the feature branch

---

## 🎓 Learning Outcome

By following this guide, you’ve:

* Set up Git safely and cleanly
* Built Git confidence using VS Code
* Protected your main branch
* Learned how to enforce PRs
* Gained experience in branching, merging, GitHub Actions
* Prepared for team collaboration & job-ready Git skills

---

Happy version-controlling 🚀
