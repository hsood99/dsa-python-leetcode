## 📘 Summary of Topics Covered

This module explains how to analyze the **time and space complexity of algorithms based on input constraints**, including both theoretical and practical perspectives.

### ✅ Key Topics Included

- **What is Time Complexity?**
  - Big O Notation: O(1), O(log n), O(n), O(n log n), O(n²), O(2^n), O(n!)
  - Understanding how runtime grows with input size

- **Estimating Feasibility Using Constraints**
  - Estimating allowed operations from constraints like `n ≤ 10⁵`, `n ≤ 10⁶`, etc.
  - When to use O(n), O(n log n), or avoid O(n²)
  - Rules of thumb based on 1s or 2s time limit per test case

- **Execution Time Guidelines**
  - Estimating how many operations Python or C++ can handle
  - Common time limits in contests and interviews

- **Logarithmic Time Complexity (O(log n))**
  - Step-by-step explanation of Binary Search
  - Why dividing input leads to log time complexity

- **Master Theorem & Recurrence Relations**
  - Understanding divide and conquer recurrences like `T(n) = aT(n/b) + f(n)`
  - Applying cases of Master Theorem to deduce complexity
  - Example: `T(n) = 3T(n/3) + O(n) → O(n log n)`

- **Time & Space Tradeoffs**
  - Using memory (e.g. prefix sums, memoization) to improve time
  - Recognizing when to optimize for time or space

- **Common Pitfalls & Misconceptions**
  - Misjudging nested loop complexity
  - Underestimating recursive call depth
  - Confusing average-case with worst-case analysis

- **Empirical Analysis**
  - Script to benchmark time/memory usage
  - Comparing brute force vs optimized solutions

- **Quick Assessments & Exercises**
  - Concept-check questions
  - Hands-on practice ideas based on input limits

---

📂 See the detailed breakdown in [`notes.md`](./notes.md)

🧪 Check the runtime analyzer in [`analyze_complexity.py`](./analyze_complexity.py)

