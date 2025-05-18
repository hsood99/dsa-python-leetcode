# Git Internals - Deep Dive Notes

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

- `.git/objects/` - Stores all Git objects (compressed and hashed)
- `.git/refs/` - Stores references to branch heads, tags, and remotes
- `.git/HEAD` - Points to the current branch or commit
- `.git/index` - Staging area information (also called the cache)

---

## 3. How Git Tracks Changes

Git tracks **content** rather than files. It snapshots content in commits instead of storing differences like other VCS.

- When you commit, Git creates a tree object representing the project state
- Each commit points to one tree and parent commits (except root commit)
- The commit history forms a Directed Acyclic Graph (DAG)

---

## 4. The Role of the Index (Staging Area)

- The **index** is a binary file that stores a snapshot of your next commit
- It acts as a buffer between your working directory and your commit history
- You add changes to the index using `git add`

---

## 5. Branches and HEAD

- Branches are simply pointers (refs) to commits
- `HEAD` is a special pointer that refers to the current branch or commit
- Moving `HEAD` changes your working directory to the commit it points to

---

## 6. How Merging Works Internally

- Git finds the **merge base** (common ancestor commit) for the branches to merge
- It performs a 3-way merge between the merge base and the two branch tips
- If conflicts arise, Git marks files as conflicted for manual resolution

---

## 7. Understanding Refs and Reflog

- **Refs:** Human-readable names pointing to commits (branches, tags)
- **Reflog:** Local history of where refs have pointed over time, useful for recovering lost commits

---

## 8. Packfiles and Garbage Collection

- Git compresses objects into **packfiles** for efficient storage and transfer
- Garbage collection (`git gc`) cleans up unreachable objects and optimizes repository size

---

## 9. Common Git Internals Commands

- `git cat-file -t <hash>`: Shows object type (commit, tree, blob, tag)
- `git cat-file -p <hash>`: Displays object content
- `git rev-parse <ref>`: Resolves refs to commit hashes
- `git ls-tree <tree-ish>`: Shows tree contents
- `git log --graph --oneline --all`: Visualizes commit DAG

---

## 10. How Push and Fetch Work

- Push sends your local commits to the remote repository
- Fetch updates your remote tracking branches without merging
- Pull = Fetch + Merge (or Rebase)

---

## 11. Summary of Key Concepts Discussed

- Git stores everything as objects identified by SHA-1
- Branches are simple pointers to commits; HEAD points to the current one
- The index stages changes for commits
- Merge is a 3-way process using a common ancestor
- Packfiles optimize storage
- Reflog helps recover lost commits
- Branch protection and PR rules do not interfere with Git internals but help workflow governance

---

Understanding these internal mechanisms empowers you to use Git with confidence and troubleshoot tricky scenarios.

---

*Happy Git mastering!* 🚀
