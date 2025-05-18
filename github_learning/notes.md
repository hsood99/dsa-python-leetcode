# 📘 Git & GitHub Learning Notes

Welcome to the complete notes on Git and GitHub based on our learning journey in this chat. This document aims to consolidate everything discussed — from basic commands to advanced concepts like PR workflows, protected branches, and GitHub Actions. It is your **one-stop reference**.

---

## 🔧 Git Basics

### 🔹 Installation

* Download from [https://git-scm.com/downloads](https://git-scm.com/downloads) – ✅ Safe and recommended.
* Prefer default settings during installation.
* For SSL, choosing `Use the native Windows Secure Channel library` is fine (default).

### 🔹 Initial Configuration

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Do this per machine/account combo.

---

## 📁 Repo Setup (Your Learning Repo)

### Structure Summary

```
dsa-python-learning/
├── README.md               # Overall purpose & layout
├── notes.md                # Master index
├── dsa/                    # DSA problems
├── python_basics_and_advanced/  # Python topics
├── github_learning/        # This folder - Git/GitHub insights
```

Each subfolder has:

* `README.md` — overview
* `notes.md` — in-depth topic explanations
* `solutions.py` or `scripts/` — code/practical examples

---

## 🌿 Branching Strategy

* Create topic-specific branches like `feature/add-array-notes`

```bash
git checkout -b feature/branch-name
```

* After adding content:

```bash
git add .
git commit -m "Add notes for XYZ"
git push origin feature/branch-name
```

---

## 🔀 Pull Requests (PRs)

* Main branch is **protected**: No direct push allowed.
* PR required for all changes.
* Workflow:

  1. Push changes to feature branch
  2. Create a PR from `feature/*` → `main`
  3. Review & merge via GitHub
  4. Optionally delete branch after merge:

```bash
git branch -d feature/my-branch
git push origin --delete feature/my-branch
```

> 📌 Tip: No need to merge main → feature again unless necessary. Just raise PR to main.

---

## 🚨 Protected Branch Rules

* Set in **GitHub → Repo Settings → Branches → Protection Rules**

  * Require PR before merging
  * Block force pushes
  * Include admins (checkbox must be ticked)

Now pushing to `main` directly gives error:

```
! [remote rejected] main -> main (protected branch hook declined)
```

This means: create branch → commit → push → raise PR

---

## 🔗 Remote Setup

* For new machine:

```bash
git remote -v           # Check remotes
git remote add origin <repo-url>
```

---

## 📬 GitHub Notifications

### Trigger Email on Push

* Settings → Webhooks/Notifications → Email → Add push notifications
* You can specify email addresses to notify on events

---

## 🤖 GitHub Actions

### Directory

```
.github/
└── workflows/
    └── python-test.yml
```

### Sample Workflow (Multi-OS)

```yaml
name: Python Test
on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: pytest
```

---

## 🛡️ Common Errors & Fixes

* `LF will be replaced by CRLF` → Ignore unless formatting issues arise.
* `nothing to commit, working tree clean` → No file changes detected.
* `feature/* not showing in GitHub` → Ensure file changes are committed and pushed.
* `remote rejected (protected branch)` → Must raise PR for protected branches.

---

## 🧠 Tips & Best Practices

* Always write meaningful commit messages
* Protect main branches
* Use branches per feature/topic
* Use PRs even in personal repos for discipline and review
* Keep markdown notes + solutions side by side

---

## ✅ GitHub Learning Directory Structure Recap

```
github_learning/
├── README.md
├── notes.md                # <- This file
├── git_basics/
│   └── notes.md
├── branching_merging/
│   └── notes.md
├── github_advanced/
│   ├── notes.md
│   └── workflows/
├── git_internals/
│   └── notes.md
└── tips_tricks/
    └── notes.md
```

Each section is optional but helps deepen mastery.

---

## 🧾 Credits

Maintained by Hitesh Sood. This repo serves as a personal learning journal and resource for others exploring Git and GitHub.

---

Happy committing! 🚀
