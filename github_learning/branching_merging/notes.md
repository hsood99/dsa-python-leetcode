# Branch Merging in Git & GitHub - Complete Notes

This `notes.md` file contains everything you need to know about **branch merging** in Git and GitHub — from basic to advanced workflows, as discussed throughout our chat.

---

## 📌 What is Branch Merging?

Branch merging is the process of integrating changes from one branch (usually a feature or dev branch) into another branch (usually the `main` or `develop` branch).

---

## 🧠 Why Use Branches?

* Work on isolated features or bug fixes.
* Collaborate without disturbing `main`.
* Simplify code reviews and version control.

---

## 🔀 Common Types of Merging

### 1. **Fast-forward Merge**

* Happens when the target branch has not diverged.
* Simply moves the pointer forward.

```bash
git checkout main
git merge feature-branch
```

### 2. **Three-way Merge**

* When both branches have diverged.
* Git creates a new merge commit.

```bash
git checkout main
git merge feature-branch
```

### 3. **Squash and Merge**

* Combines all commits into one for a clean history.
* Used via GitHub Pull Request UI.

### 4. **Rebase and Merge**

* Rewrites the feature branch commits on top of target branch.
* Used to avoid merge commits, creating linear history.

```bash
git checkout feature-branch
git rebase main
```

---

## 🌿 Workflow for Safe Merging

1. Create a feature branch:

```bash
git checkout -b feature/xyz
```

2. Commit and push changes:

```bash
git add .
git commit -m "Add XYZ feature"
git push origin feature/xyz
```

3. Raise a Pull Request (PR) from `feature/xyz` to `main`.
4. Review and merge the PR.
5. Optionally delete the branch:

```bash
git branch -d feature/xyz
# and on GitHub:
git push origin --delete feature/xyz
```

---

## 🔐 Protected Branches & PR Rules

### What Are Protected Branches?

* Branches like `main` can be protected to avoid direct pushes.
* Enforces merging via PRs only.

### Setup via GitHub:

1. Go to `Settings > Branches`.
2. Add a branch rule for `main`.
3. Enable options like:

   * ✅ Require pull request before merging
   * ✅ Require status checks to pass
   * ✅ Include administrators

Now, direct pushes to `main` are blocked:

```
! [remote rejected] main -> main (protected branch hook declined)
```

---

## 📬 Raising a Pull Request (PR)

### From GitHub UI:

* Push to feature branch
* Click "Compare & Pull Request"
* Add description and submit

### From VS Code:

* Install **GitHub Pull Requests and Issues** extension
* Use Source Control panel or Command Palette

---

## 🧪 Syncing Branches

### To keep your feature branch updated with `main`:

```bash
git checkout feature/xyz
git pull origin main --rebase
```

### To merge main into feature branch (if needed):

```bash
git checkout feature/xyz
git merge main
```

---

## 🧼 Cleaning Up Branches

* After merging a feature branch:

```bash
git checkout main
git branch -d feature/xyz
git push origin --delete feature/xyz
```

* `-d` = delete local branch
* `--delete` = delete remote branch

---

## 📝 Pro Tips

* **Always pull latest main before creating a new branch.**
* **Use descriptive branch names** like `feature/add-login-page`.
* **Prefer PR-based merges** to enable review workflows.
* **Enable PR rules** on protected branches for better collaboration.

---

## ✅ Summary

This guide covered:

* Types of merges
* Clean merge workflows
* Protected branches
* PR setup
* Best practices for local & remote branch handling

You’re now equipped to confidently manage branching and merging in real-world development workflows. ✅
