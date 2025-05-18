# GitHub Advanced Concepts Notes 📘

This file covers all advanced GitHub workflows and configurations including Personal Access Tokens, Protected Branches, Pull Requests, Email Notifications, and GitHub Actions.

---

## 🔐 1. Personal Access Tokens (PAT)

Personal Access Tokens are used to authenticate Git operations instead of using your GitHub password.

### 🔧 Steps to Generate PAT:

1. Go to your GitHub profile → `Settings`
2. Navigate to `Developer Settings` → `Personal Access Tokens`
3. Click `Generate new token` → Select scopes like:

   * `repo`
   * `workflow`
   * `user`
4. Copy and store it safely (you won’t see it again).

### 🔒 Usage:

Use PAT when pushing from terminal:

```bash
git push origin main
# Enter PAT when prompted for password
```

---

## 🔐 2. Protected Branches

Protected branches prevent unauthorized or accidental direct pushes to important branches like `main`.

### 🚧 How to Enable:

1. Go to your repo → `Settings` → `Branches`
2. Add a branch protection rule for `main`
3. Enable:

   * ✅ Require pull request before merging
   * ✅ Require status checks (optional)
   * ✅ Include administrators

### 🔁 Result:

* Pushing directly to `main` will now throw an error
* All changes must go through a pull request (PR)

---

## 🔁 3. Pull Requests (PR)

Pull Requests allow you to propose changes in one branch and merge them into another (usually `main`).

### 🔧 Create PR Flow:

```bash
git checkout -b feature/my-change
# Make changes

git add .
git commit -m "Add my change"
git push origin feature/my-change
```

Then:

* Go to GitHub UI → Compare & pull request
* Add title, description, and create PR
* Review → Merge → Delete branch (optional)

### ✅ Benefits:

* Enforces code review
* Prevents accidental pushes
* Tracks changes clearly

---

## 📧 4. Email Notifications for Events

GitHub allows sending email notifications on specific events like Push, PR, etc.

### 🔧 Enable Email Notifications:

1. Go to `Settings` → `Webhooks` or `Email Notifications`
2. Add your email
3. Choose events (push, PR opened, merged, etc.)

### 📌 Note:

You may also set up **GitHub Actions** to send custom emails via workflow steps (e.g., using Mailgun, Gmail SMTP, or SendGrid).

---

## ⚙️ 5. GitHub Actions

GitHub Actions lets you automate workflows like testing, deployments, notifications, etc.

### 📁 Structure:

Create file: `.github/workflows/main.yml`

### 🧪 Example: Run Python Tests

```yaml
name: Python Test

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        pytest
```

### ✅ Benefits:

* Continuous Integration (CI)
* Auto email/slack alerts
* Works cross-platform

---

## 🔄 6. GitHub Forks vs Branches

* **Fork:** Creates a copy of the repository to another account (used in open source contributions).
* **Branch:** Creates a separate line of development within the same repo.

### 🔍 Your Case:

You own the repo, so you don’t fork. Instead:

* Create feature branches → Push → Create PR → Merge to `main`

---

## ⚠️ Error Handling

### 🔒 Push Rejected (Protected Branch)

```bash
error: failed to push some refs to 'origin/main'
```

🔧 Fix: Push to another branch and raise PR.

### ⛔ Remote Rejected

```bash
! [remote rejected] main -> main (protected branch hook declined)
```

🔧 Cause: Branch protection is active.

---

## 📁 Folder & File References

You can organize GitHub learning content like:

```
github_learning/
├── github_advanced/
│   ├── notes.md
│   ├── README.md
│   └── examples/
```

---

Happy Automating & Collaborating! 🚀
