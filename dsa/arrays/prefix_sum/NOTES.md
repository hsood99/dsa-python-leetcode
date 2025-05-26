# 📘 Prefix Sum: Complete Notes (Week 1 - Arrays & Hashing)

## ✅ What is Prefix Sum?

Prefix Sum is a technique for preprocessing cumulative sums of elements in an array. It allows us to answer subarray or range sum queries efficiently in constant time after O(n) preprocessing.

---

## 🔢 Core Concept

Given an array `nums`, we define a prefix sum array `prefix` as:

```python
prefix[0] = nums[0]
prefix[i] = prefix[i-1] + nums[i]
```

Or with 1-based indexing:

```python
prefix[0] = 0
prefix[i] = prefix[i-1] + nums[i-1]
```

To calculate the sum from index `i` to `j`:

```python
sum(i, j) = prefix[j+1] - prefix[i]  # with 1-based offset
```

---

## 🧠 Why Prefix Sum?

* O(n) time to compute prefix
* O(1) time to compute sum of any subarray
* Very useful for multiple queries or range-based problems

---

## 📚 Common Patterns and LeetCode Problems

### 🔹 1. Range Sum Query

Compute the sum of elements in range \[l, r] efficiently.

```python
prefix = [0] * (len(nums) + 1)
for i in range(len(nums)):
    prefix[i+1] = prefix[i] + nums[i]

# sum of nums[l...r]
range_sum = prefix[r+1] - prefix[l]
```

**Problems:**

* [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
* [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)

---

### 🔹 2. Subarray Sum Equals K

Count number of subarrays whose sum equals k.

```python
count = 0
prefix = 0
prefix_map = {0: 1}

for num in nums:
    prefix += num
    count += prefix_map.get(prefix - k, 0)
    prefix_map[prefix] = prefix_map.get(prefix, 0) + 1
```

**Problems:**

* [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

---

### 🔹 3. Maximum Sum of Fixed-Size Subarray

Find the max sum of subarray of size `k`.

```python
prefix = [0] * (len(nums) + 1)
for i in range(len(nums)):
    prefix[i+1] = prefix[i] + nums[i]

max_sum = 0
for i in range(k, len(prefix)):
    max_sum = max(max_sum, prefix[i] - prefix[i-k])
```

**Problems:**

* [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)

---

### 🔹 4. Binary Array / Odd Numbers Count

Count subarrays with exactly `k` odd numbers by converting array to binary form (0/1).

**Problems:**

* [1248. Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)
* [930. Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/)

---

### 🔹 5. Prefix Sum + Binary Search

Used when asked for shortest/longest subarray with sum ≥ target.

```python
import bisect

prefix = [0]
for num in nums:
    prefix.append(prefix[-1] + num)

min_len = float('inf')
for i in range(len(prefix)):
    target_sum = prefix[i] + target
    bound = bisect.bisect_left(prefix, target_sum)
    if bound < len(prefix):
        min_len = min(min_len, bound - i)
```

**Problems:**

* [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

---

### 🔹 6. 2D Prefix Sum (Matrix)

Efficiently compute sum of submatrix \[r1,c1] to \[r2,c2].

```python
for r in range(m):
    for c in range(n):
        prefix[r+1][c+1] = matrix[r][c] + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c]
```

**Problems:**

* [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)
* [1277. Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

---

## 🧠 When to Use Prefix Sum

| Situation                         | Use Prefix Sum? | Notes                            |
| --------------------------------- | --------------- | -------------------------------- |
| Multiple range sum queries        | ✅               | Use precomputed prefix           |
| Count subarrays with specific sum | ✅               | Prefix + hashmap pattern         |
| Need dynamic updates              | ❌               | Use Segment Tree/Fenwick Tree    |
| Fixed size sliding window         | ✅/🔁            | Can use prefix or sliding window |

---

## 🚫 Common Mistakes

* Off-by-one errors in prefix indexing.
* Forgetting to initialize `prefix[0] = 0`.
* Misusing prefix sums for dynamic problems.

---

## 🧪 Practice Problems Summary

| Level  | Problems                                                                                                                                                                                                                                                             |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Easy   | [303](https://leetcode.com/problems/range-sum-query-immutable/), [1732](https://leetcode.com/problems/find-the-highest-altitude/)                                                                                                                                    |
| Medium | [560](https://leetcode.com/problems/subarray-sum-equals-k/), [209](https://leetcode.com/problems/minimum-size-subarray-sum/), [1248](https://leetcode.com/problems/count-number-of-nice-subarrays/), [930](https://leetcode.com/problems/binary-subarrays-with-sum/) |
| Hard   | [862](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/), [363](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)                                                                                                             |

---

## 🧩 Prefix Sum in Upcoming Topics (Do Not Miss)

> These are not covered here but build upon your prefix knowledge:

| Topic                                  | Usage                                                                            |
| -------------------------------------- | -------------------------------------------------------------------------------- |
| **Week 3 - Sliding Window**            | Compare vs prefix sum for max/min subarray problems (e.g., max sum window)       |
| **Week 4 - Recursion & Binary Search** | Binary search on prefix array (e.g., \[209]) or recursively divide prefix ranges |
| **Week 5 - Trees & Graphs**            | Tree-based prefix sums for subtree queries or Euler tour prefixing               |
| **Week 6 - Dynamic Programming**       | Prefix in recurrence optimizations (e.g., cumulative DP transitions)             |
| **Week 7 - Heaps/Tries**               | Not direct prefix sums but occasionally used for scoring/counting prefixes       |

---

## ✅ Final Thoughts

Prefix sum is one of the most powerful tools in array preprocessing. Mastering it will help in many range-related and subarray-based LeetCode problems. Prefix Sum + Hashmap is one of the most used techniques for interview problems.

---

Feel free to use this `.md` file in your GitHub repo for reference and revision.
