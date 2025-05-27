# 📘 Arrays & Hashing - Week 1 DSA Notes

This note summarizes all important concepts, patterns, and LeetCode problems you must master in **Week 1: Arrays & Hashing**.

---

## ✅ 1. Prefix Sum

**Concept**: Convert expensive range-sum queries into constant-time lookups after O(n) preprocessing.

**1D Patterns:**

* Basic range sum with prefix array
* Subarray sum equals k using prefix + hashmap
* Fixed-size subarray max/min sum using prefix
* Variable size subarrays with binary search + prefix

**2D Prefix:**

* Matrix region sum queries in O(1)

**Common Tricks:**

* Prefix\[i] = Prefix\[i-1] + nums\[i]
* To find sum(i to j): Prefix\[j] - Prefix\[i-1]

**LeetCode:**

* 303, 560, 930, 209, 304

📁 See `prefix_sum/notes.md`

---

## ✅ 2. Hash Map / Hash Set

**Concept**: Constant time lookup/insertion/deletion to store frequency, index, uniqueness.

**Patterns:**

* Frequency counter
* Index tracking
* Hash set for duplicates or uniqueness
* Combined with prefix sum for optimized search

**Common Use Cases:**

* Check if two arrays contain same elements
* Store visited items
* Track window character counts

**LeetCode:**

* 1, 217, 36, 383, 349

---

## ✅ 3. Sliding Window

**Concept**: Efficiently handle subarrays of fixed or variable lengths in O(n) time.

**Patterns:**

* Fixed size window (sum/average/max)
* Variable size (longest/shortest substring satisfying constraint)
* Window with hashmap for char frequency tracking

**LeetCode:**

* 239, 3, 76, 438, 643

🔜 Deep dive in **Week 3**

---

## ✅ 4. Two Pointers

**Concept**: Use two pointers moving through array to optimize brute force O(n²) to O(n)

**Patterns:**

* Sorted array → Opposite ends inward
* Fast and slow pointer
* In-place overwrite

**LeetCode:**

* 26, 27, 283, 125, 167

---

## ✅ 5. Binary Search on Arrays

**Concept**: Efficient search on sorted arrays

**LeetCode:**

* 704, 34, 35

🔜 Will be used heavily in recursion/search week

---

## ✅ 6. Array Techniques

**Concepts:**

* In-place reversal, rotation
* Cyclic replacements
* Element placement by value/index

**LeetCode:**

* 189, 41, 134, 152

---

## 🧠 Core Ideas

| Concept          | Notes                                               |
| ---------------- | --------------------------------------------------- |
| Prefix Sum       | For range sum, subarray sum                         |
| Hash Map / Set   | Count freq, check duplicates, lookup                |
| Sliding Window   | Efficient range processing (avg, longest, shortest) |
| Two Pointers     | Optimize nested loops                               |
| Binary Search    | For sorted arrays, search-based problems            |
| Array Transforms | Rotation, in-place edits, position-based tricks     |

---

## 🧩 Suggested Practice

* ✅ 5–7 Easy (basic hashing, frequency count, prefix sum)
* ✅ 10–12 Medium (subarray sums, sliding window, two pointers)
* ✅ 3–5 Hard (prefix + hashmap, sliding window max, minimum window substring)

---

## 🔮 Covered Later (Don’t Miss)

| Topic               | When?  | Why It Matters                                      |
| ------------------- | ------ | --------------------------------------------------- |
| Sliding Window Deep | Week 3 | Longest substring, max window value, character freq |
| Recursion + Prefix  | Week 4 | Used in backtracking with sums                      |
| Trees + Prefix Path | Week 5 | Path Sum problems in trees                          |
| Dynamic Programming | Week 6 | Prefix optimization in Kadane-like problems         |

---

> "Arrays & Hashing" are the foundation. Mastering these patterns sets the stage for every DSA category ahead.

---

📂 Next Module → **Linked Lists (Week 2)**
