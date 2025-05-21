# 🧠 Time & Space Complexity Analysis – Full Notes

This document is a **comprehensive guide** to mastering complexity analysis. It covers everything discussed in our chat: from basic definitions, real-world estimation using constraints, to theoretical tools like the Master Theorem and recursion analysis.

---

## 📌 1. What is Time Complexity?

Time complexity describes how the **execution time** of an algorithm changes with input size `n`.

### 🔹 Common Complexities

| Big O      | Name         | Description                                |
| ---------- | ------------ | ------------------------------------------ |
| O(1)       | Constant     | Independent of input size                  |
| O(log n)   | Logarithmic  | Input is halved (e.g., Binary Search)      |
| O(n)       | Linear       | Proportional to input                      |
| O(n log n) | Linearithmic | Divide-and-conquer algorithms              |
| O(n^2)     | Quadratic    | Double nested loops                        |
| O(2^n)     | Exponential  | Recursive branching (e.g., subsets)        |
| O(n!)      | Factorial    | All permutations (e.g., TSP, backtracking) |

---

## 📌 2. What is Space Complexity?

Space complexity refers to the **amount of memory** required by an algorithm in relation to the input size `n`.

* Includes input storage, auxiliary space, and call stack (in recursion).
* Similar analysis technique as time complexity.

### 🔹 Example:

```python
def sum_array(arr):
    total = 0            # O(1)
    for num in arr:      # O(n)
        total += num
    return total         # Total space: O(1)
```

---

## 🧪 3. Estimating Time Complexity from Constraints

| Input Size `n`  | Feasible Time Complexity |
| --------------- | ------------------------ |
| `n ≤ 10`        | `O(n!), O(2^n)`          |
| `n ≤ 100`       | `O(n^3), O(n^2 log n)`   |
| `n ≤ 1,000`     | `O(n^2)`                 |
| `n ≤ 100,000`   | `O(n log n)`             |
| `n ≤ 1,000,000` | `O(n)`                   |

> Approximate max ops in 1s:
>
> * **C++** ≈ 10^8 operations
> * **Python** ≈ 10^7 operations

### 🔍 Example: Constraint-Based Analysis

For a problem with `n ≤ 10^5` and 1s time limit:

* A brute-force O(n^2) solution (10^10 ops) is too slow.
* Need O(n log n) or better.

---

## 📐 4. Deriving Complexity via Recurrence Relations

Many recursive algorithms form equations like:
$T(n) = aT(n/b) + f(n)$

### 🔹 Master Theorem Cases:

1. **Case 1:** $f(n) = O(n^{\log_b a - \epsilon})$ → $T(n) = \Theta(n^{\log_b a})$
2. **Case 2:** $f(n) = \Theta(n^{\log_b a})$ → $T(n) = \Theta(n^{\log_b a} \cdot \log n)$
3. **Case 3:** $f(n) = \Omega(n^{\log_b a + \epsilon})$ → $T(n) = \Theta(f(n))$

### ✅ Example:

$T(n) = 3T(n/3) + O(n)$

* a = 3, b = 3 → $\log_b a = 1$
* f(n) = O(n) = $\Theta(n^{\log_b a})$
  ➡ Case 2 → $T(n) = \Theta(n \log n)$

---

## 🔍 5. Logarithmic Time Explained (O(log n))

### 🧠 Why log n?

Take n = 16. Divide in half repeatedly:

* Step 1: 16 → 8
* Step 2: 8 → 4
* Step 3: 4 → 2
* Step 4: 2 → 1
  Total steps = 4 = $\log_2 16$

➡ **Binary Search**, **Tree height**, and some **divide-and-conquer** algorithms fall under this.

---

## 🧪 6. Measuring Complexity Empirically

Python script to profile time and space:

```python
import time
import tracemalloc

def analyze_complexity(func, *args, **kwargs):
    tracemalloc.start()
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"\nFunction: {func.__name__}")
    print(f"Execution Time: {(end_time - start_time):.6f} seconds")
    print(f"Peak Memory Usage: {peak / 1024:.2f} KB")
    return result
```

### 📘 Sample: Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Usage
if __name__ == "__main__":
    from analyze_complexity import analyze_complexity
    arr = list(range(10**6))
    analyze_complexity(binary_search, arr, 999999)
```

---

## ⚠️ 7. Pitfalls & Misconceptions

* ❌ Assuming `O(n^2)` is fine for `n = 10^5`
* ❌ Ignoring base cases in recursion complexity
* ❌ Mistaking average-case for worst-case
* ❌ Not counting recursive calls in space complexity
* ✅ Always validate algorithm vs worst input size

---

## 📘 8. Questions to Test Your Understanding

1. What is the time complexity of this code?

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

> A: O(n^2)

2. What complexity is safe for n = 10^6 in Python?

> A: O(n), O(n log n)

3. You halve n each time in a loop. How many iterations?

> A: O(log n)

4. What is the time complexity of binary search?

> A: O(log n)

---

## 🧩 9. Suggested Exercises

1. Write two versions of checking if an array is sorted:

   * O(n)
   * O(n^2)

2. Derive time complexity for:

   * Merge Sort
   * Fibonacci with and without memoization

3. Solve recurrence:

   * T(n) = 2T(n/2) + n^2
   * T(n) = T(n/2) + 1

4. Use `analyze_complexity` on:

   * Linear search
   * Merge sort
   * Binary search

---

## 📁 10. Recommended Folder Structure

```
complexity_analysis/
├── README.md
├── notes.md
├── analyze_complexity.py
└── examples/
    ├── binary_search.py
    ├── merge_sort_profiled.py
    └── brute_vs_optimized.py
```

---

## ✅ Final Takeaway

Understanding complexity analysis helps you:

* Predict algorithm scalability
* Avoid TLE (Time Limit Exceeded)
* Select optimal approaches based on input size
* Write clean and efficient code

➡ After mastering this, you’ll be equipped to analyze any algorithm confidently!
