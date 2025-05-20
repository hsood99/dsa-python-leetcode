# 📚 Week 3: Stacks & Queues – Mastery Level

Welcome to **Week 3** of the DSA Mastery Journey!  
This week is focused on building **expert-level skills** in **Stacks and Queues** — essential for solving a wide range of **interview and competitive coding** problems.

---

## 🧠 Topics Covered

### 🔹 1. Stack – LIFO (Last In First Out)
- Basic operations: `push()`, `pop()`, `peek()`
- Implementing with Python `list`
- Applications: Backtracking, Expression Evaluation, Undo feature

### 🔹 2. Queue – FIFO (First In First Out)
- Basic operations: `enqueue()`, `dequeue()`, `peek()`
- Python implementation: `collections.deque`
- Applications: Scheduling, BFS, Producer-Consumer

### 🔹 3. Monotonic Stack
- What is it: Stack that keeps elements in sorted (monotonic) order
- Monotonic Increasing & Decreasing Stack
- Optimizes problems involving **Next Greater/Smaller Element**, etc.
- **Important Pattern**: Push while popping smaller elements for "next greater"

### 🔹 4. Monotonic Queue
- Used for sliding window problems where you need max/min
- Maintains a decreasing or increasing deque
- Key problem: **Sliding Window Maximum** in O(n)

### 🔹 5. Sliding Window Maximum
- Naive solution: O(n * k)
- Optimal: **Monotonic Deque**
- Real-world use cases: Max CPU usage, stock prices, etc.

### 🔹 6. Min Stack (Stack with `getMin()` in O(1))
- Approach 1: Two stacks (main + min)
- Approach 2: Space-optimized using difference (delta encoding)
- Interview favorite

### 🔹 7. LRU Cache (Least Recently Used)
- Implemented with **HashMap + Doubly Linked List**
- Python `OrderedDict` alternative
- O(1) for `get()` and `put()`
- Explains Linked List integration with Hash Maps

### 🔹 8. Next Greater Element Problems
- **Next Greater Element I** – `nums1` subset of `nums2`
- **Next Greater Element II** – Circular version
- Use of stack + map in linear time
- Generalized template for future variants

### 🔹 9. Largest Rectangle in Histogram
- Classic hard monotonic stack problem
- Find area with each bar as smallest height
- Requires understanding of:
  - **Previous Smaller Element**
  - **Next Smaller Element**
- Used in solving problems like **Maximal Rectangle**

### 🔹 10. Queue Implementations
- Stack using two Queues
- Queue using two Stacks
- Covers low-level understanding of both

### 🔹 11. Stack-based Evaluation Problems
- **Valid Parentheses**
- **Evaluate Reverse Polish Notation (RPN)**
- **Basic Calculator I/II**

---

## 🔁 Revisited Topics (coming in Week 4, but worth early awareness)
> These involve stack but are part of **Recursion / DFS / Backtracking**, not Week 3 directly.
- Stack in Recursion
- DFS using stack
- Backtracking using implicit call stack

---

## 📂 Directory Structure
```
week3/
├── README.md # ✅ You are here
├── stack_basics.py
├── queue_basics.py
├── monotonic_stack/
│ ├── next_greater_element.py
│ ├── next_greater_element_circular.py
│ ├── largest_rectangle.py
├── monotonic_queue/
│ └── sliding_window_maximum.py
├── lru_cache/
│ ├── lru_linked_list.py
│ └── lru_ordered_dict.py
├── min_stack/
│ ├── min_stack_two_stacks.py
│ └── min_stack_delta_encoding.py
├── evaluation_problems/
│ ├── valid_parentheses.py
│ ├── reverse_polish_notation.py
│ └── basic_calculator.py
```

---

## ✅ Must-Solve LeetCode Problems

| Problem | Type |
|--------|------|
| [155. Min Stack](https://leetcode.com/problems/min-stack/) | Stack |
| [146. LRU Cache](https://leetcode.com/problems/lru-cache/) | LRU |
| [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Monotonic Stack |
| [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | Monotonic Stack (Circular) |
| [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Monotonic Queue |
| [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Monotonic Stack |
| [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack |
| [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Stack |
| [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | Stack |

---

## 🎯 Goals for the Week

- [x] Master Monotonic Stack & Queue
- [x] Implement LRU Cache from scratch
- [x] Understand stack-based evaluation problems
- [x] Solve at least **20–25** high-quality problems
- [x] Time & space complexity for each

---

## 🧩 Tips & Patterns

- Monotonic Stack is your best tool for NGE/NSG/Largest Area problems
- Always track indices in stack/queue, not values
- For space optimization in Min Stack, use `diff = x - min`
- Don't memorize solutions — **master the patterns**

---

## 📎 What's Next?

➡️ Head to [Week 4: Recursion, Backtracking, DFS](../week4/README.md)

