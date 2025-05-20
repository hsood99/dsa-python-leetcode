# Week 3: Stacks & Queues - Expert Notes

This document contains complete notes for mastering Week 3 topics in Data Structures and Algorithms: Stacks & Queues. It includes in-depth explanations, code snippets, and tips to help you solve any LeetCode or interview problem in this domain.

---

## 1. Stack Basics

### Definition:

A **Stack** is a linear data structure that follows the **Last In First Out (LIFO)** principle.

### Operations:

* `push(x)`: Add element to top
* `pop()`: Remove top element
* `peek()/top()`: View top element without removing
* `isEmpty()`: Check if stack is empty

### Python Example:

```python
stack = []
stack.append(10)
stack.append(20)
print(stack[-1])  # 20
stack.pop()
```

---

## 2. Queue Basics

### Definition:

A **Queue** is a linear data structure that follows the **First In First Out (FIFO)** principle.

### Operations:

* `enqueue(x)`: Add element to rear
* `dequeue()`: Remove element from front
* `peek()`: View front element

### Python Example:

```python
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
print(queue[0])  # 10
queue.popleft()
```

---

## 3. Monotonic Stack

### Concept:

A **Monotonic Stack** is a stack that maintains its elements in sorted order (increasing or decreasing).

* **Increasing Stack**: for Next Greater Element
* **Decreasing Stack**: for Next Smaller Element

### Usage:

* Efficiently solve problems where you need to find the next/previous greater/smaller element

### Template:

```python
stack = []
for i in range(len(nums)):
    while stack and nums[i] > nums[stack[-1]]:
        index = stack.pop()
        res[index] = nums[i]
    stack.append(i)
```

---

## 4. Monotonic Queue

### Concept:

A **Monotonic Queue** is a double-ended queue (deque) that maintains elements in increasing or decreasing order.

* Used in **sliding window maximum/minimum** problems

### Python Example:

```python
from collections import deque
def maxSlidingWindow(nums, k):
    dq, res = deque(), []
    for i in range(len(nums)):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and nums[i] > nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
```

---

## 5. Min Stack

### Problem:

Implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.

### Approach 1: Two Stacks

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
```

### Approach 2: Space Optimized

Use difference between element and min:

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, x):
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            diff = x - self.min
            self.stack.append(diff)
            if diff < 0:
                self.min = x

    def pop(self):
        top = self.stack.pop()
        if top < 0:
            self.min = self.min - top

    def top(self):
        top = self.stack[-1]
        return self.min if top < 0 else self.min + top

    def getMin(self):
        return self.min
```

---

## 6. LRU Cache

### Problem:

Design a cache that supports `get()` and `put()` in O(1).

### Approach:

* Use a **HashMap** for key lookups
* Use a **Doubly Linked List** for recent usage order

### Python Example using `OrderedDict`:

```python
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

---

## 7. Next Greater Element I

### Problem:

Find next greater element for nums1\[i] in nums2

### Monotonic Stack Solution:

```python
def nextGreaterElement(nums1, nums2):
    stack, nge = [], {}
    for num in nums2:
        while stack and num > stack[-1]:
            nge[stack.pop()] = num
        stack.append(num)
    return [nge.get(num, -1) for num in nums1]
```

---

## 8. Largest Rectangle in Histogram

### Problem:

Find the area of the largest rectangle in the histogram.

### Stack Approach:

```python
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area
```

---

## 9. Stack Evaluation Problems

### Valid Parentheses:

```python
def isValid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack
```

### Evaluate Reverse Polish Notation:

```python
def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token not in '+-*/':
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            else: stack.append(int(a / b))
    return stack[0]
```

---

## 10. Patterns & Tips

* Always store **indices** in stack for Next Greater/Smaller problems
* Min Stack with delta saves space
* Use deque for sliding window problems
* Monotonic structure helps reduce brute-force O(n\*k) to O(n)

---

## ✅ You are now ready to solve all problems in Week 3 with confidence!
