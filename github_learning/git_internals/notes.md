# 🔍 Git Internals - Deep Dive Notes

This document explains the underlying mechanisms of Git — how it stores data, manages history, and performs operations. Understanding Git internals helps you debug complex issues and use Git more effectively.

---

## 1. Git Object Model

Git stores content as **objects** in a repository. There are four main object types:

- **Blob:** Stores file data (content only, no metadata)
- **Tree:** Stores directory listings (file names, modes, and references to blobs or other trees)
- **Commit:** Stores metadata for a commit (author, message, pointer to a tree, and parent commits)
- **Tag:** Stores references to objects with extra metadata (usually used for release tags)

All objects are identified by a SHA-1 hash of their content.

---

## 2. The Git Repository Structure

- `.git/objects/` → Stores all Git objects (compressed and hashed)
- `.git/refs/` → Stores references to branch heads, tags, and remotes
- `.git/HEAD` → Points to the current branch or commit
- `.git/index` → Staging area information (also called the cache)

---

## 3. How Git Tracks Changes

Git tracks **content**, not files.

- When you commit, Git creates a tree object representing the project state.
- Each commit points to one tree and parent commits (except the root commit).
- The commit history forms a **Directed Acyclic Graph (DAG)**.

---

## 4. The Role of the Index (Staging Area)

- The **index** is a binary file that stores a snapshot of your next commit.
- It acts as a buffer between your working directory and commit history.
- Changes are staged using:

```bash
git add <file>
```

---

## 5. Branches and HEAD

- **Branches** are simply pointers (refs) to commits.
- `HEAD` is a special reference pointing to the current branch or specific commit.
- Moving `HEAD` updates the working directory to match the pointed commit.

---

## 6. How Merging Works Internally

- Git finds the **merge base** (common ancestor) of two branches.
- Performs a **3-way merge** between:
  - Merge base
  - Tip of current branch
  - Tip of the branch being merged
- Conflicts are marked for manual resolution.

---

## 7. Understanding Refs and Reflog

- **Refs:** Human-readable names pointing to commits (branches, tags).
- **Reflog:** Local history of `HEAD` and branch tip movements. Helps recover lost work.

```bash
git reflog
```

---

## 8. Packfiles and Garbage Collection

- Git compresses many objects into **packfiles** to optimize storage and speed up transfers.
- **Garbage collection:**

```bash
git gc
```

- Removes unreachable or dangling objects.

---

## 9. Common Git Internals Commands

```bash
git cat-file -t <hash>       # Show object type
git cat-file -p <hash>       # Show object content
git rev-parse <ref>          # Resolve a ref to a full hash
git ls-tree <tree-ish>       # Show a tree's contents
git log --graph --oneline --all   # Visualize commit DAG
```

---

## 10. How Push and Fetch Work

- **Push:** Sends your commits to the remote:

```bash
git push origin main
```

- **Fetch:** Retrieves remote changes but doesn't merge:

```bash
git fetch origin
```

- **Pull:** Combines `fetch` + `merge` (or `rebase`)

```bash
git pull origin main
```

---

## 11. Summary of Key Concepts Discussed

- Git stores everything as **objects** identified by SHA-1 hashes.
- **Branches** are lightweight pointers to commits.
- The **index** stages changes before committing.
- Git performs **3-way merges** using common ancestors.
- **Packfiles** improve performance and reduce size.
- **Reflog** is a powerful recovery tool.
- Workflow rules (like PRs or branch protection) operate on top of Git, not within its internals.

---

Understanding these internals gives you an edge in using Git professionally and resolving complex problems.

---

*Happy Git mastering!* 🚀
