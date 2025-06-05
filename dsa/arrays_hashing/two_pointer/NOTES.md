# 🧭 Two Pointers: The Ultimate Visual Guide

This guide covers everything you need to master the **Two Pointers** technique in DSA and LeetCode interview prep. By the end, you'll be able to tackle any two-pointer problem with confidence.

---

## 🧠 What Is the Two Pointers Technique?

A method that uses **two indices (pointers)** to iterate through a data structure, usually:

* **From both ends**: (start and end)
* **From the same side**: one fast, one slow
* Often on **sorted data**

---

## 🚦 When to Use It?

* Finding pair(s) that match a condition
* Processing **sorted arrays** efficiently
* Shrinking search space from both sides
* Replacing **nested loops** to optimize time

---

## 🧩 Core Patterns & Examples

### 1. **Two Pointers from Both Ends**

Used when the array is **sorted** or when comparing both ends.

* **Example**: Two Sum II, Valid Palindrome

```text
[1, 2, 3, 4, 6], target = 6
 ^           ^
left       right
```

### 2. **Fast and Slow Pointer**

Used to modify in-place or find certain patterns.

* **Example**: Remove Duplicates, Move Zeroes

```text
[0, 1, 0, 3, 12]
     ^     ^
   slow   fast
```

### 3. **Window Expansion (Sliding Window)**

Used for substring/window-based problems.

* **Example**: Longest Substring Without Repeating Characters

```text
"abcabcbb"
 ^   ^
start end
```

### 4. **Partitioning and Swapping**

Used for in-place rearrangement.

* **Example**: Sort Colors, Move Zeroes

```text
[2,0,2,1,1,0] → [0,0,1,1,2,2]
```

---

## 🧪 Must-Know LeetCode Problems

### ✅ Easy

* [x] Two Sum II (167)
* [x] Valid Palindrome (125)
* [x] Squares of a Sorted Array (977)
* [x] Move Zeroes (283)
* [x] Remove Element (27)

### ⚙️ Medium

* [x] 3Sum (15)
* [x] Container With Most Water (11)
* [x] Remove Duplicates from Sorted Array (26)
* [x] Sort Colors (75)
* [x] Backspace String Compare (844)

### 🔺 Hard

* [x] Trapping Rain Water (42)
* [x] Minimum Window Substring (76)
* [x] Sliding Window Maximum (239)

---

## 🧘 Strategy Table

| Pattern           | Key Idea                      | Movement                       |
| ----------------- | ----------------------------- | ------------------------------ |
| Two Sum (Sorted)  | Use left+right to find target | move inward                    |
| Valid Palindrome  | Check alphanumeric equality   | move inward                    |
| Remove Duplicates | In-place deduplication        | fast/slow pointers             |
| Container Water   | Track max area                | shrink shorter height side     |
| Trapping Water    | Use maxLeft and maxRight      | move pointer with lower height |

---

## 🗓️ Suggested 4-Day Practice Plan

### **Day 1: Basic Practice**

* Two Sum II
* Valid Palindrome
* Squares of a Sorted Array
* Move Zeroes
* Remove Element

### **Day 2: Intermediate Patterns**

* 3Sum
* Container With Most Water
* Remove Duplicates
* Sort Colors
* Backspace String Compare

### **Day 3: Advanced Patterns**

* Trapping Rain Water
* Minimum Window Substring
* Sliding Window Maximum
* Longest Substring Without Repeating Characters

### **Day 4: Mixed Practice (Timed)**

* Mix of all levels under time pressure.

---

## 🏁 Final Tips

* Focus on pointer movement logic.
* Think: "Can I replace nested loops with 2 pointers?"
* Dry run on small inputs.
* Use visuals: draw boxes, ranges, or pointer movements.

---

You're now ready to walk through problems interactively!
