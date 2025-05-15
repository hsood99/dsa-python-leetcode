# Stacks: Definition & Core Operations

What Is a Stack?
A stack is an abstract data type where elements are added and removed at the top, following LIFO order. In LIFO, the last element pushed onto the stack is the first one popped off.

# Essential Operations (Stacks)
- push(x): Insert element x onto the top of the stack (amortized O(1)).
- pop(): Remove and return the top element; underflow occurs if the stack is empty (O(1)).
- peek()/top(): Return the top element without removing it (O(1)).
- isEmpty()/size(): Check if the stack is empty or retrieve its current size (O(1)).

# Implementations
- Array-based: Use a fixed or dynamic array with an index pointer (top). Push/pop at the end achieve amortized O(1).
- Linked-list–based: Maintain a pointer to the head of a singly linked list; push/pop at the head take O(1) and avoid overflow unless memory is exhausted.

# Common Applications
- Expression evaluation & parsing: Convert infix to postfix or prefix and evaluate using a stack of operands and operators.
- Function call management: The call stack tracks return addresses and local variables for nested or recursive calls.
- Backtracking & depth-first search (DFS): Use a stack to explore graph paths or to implement undo mechanisms in applications.
- String reversal: Push characters and pop them to reverse a string in O(n) time and space.

# Queues: Definition & Core Operations

What Is a Queue?
A queue is an abstract data type in which elements are inserted at the rear and removed from the front, following FIFO order. In FIFO, the first element enqueued is the first one dequeued.

# Essential Operations
- enqueue(x): Insert element x at the rear of the queue (O(1)).
- dequeue(): Remove and return the front element; underflow if the queue is empty (O(1)).
- peek()/front(): Return the front element without removing it (O(1)).
- isEmpty()/size(): Check if the queue is empty or retrieve its size (O(1)).

# Implementations
- Circular array: Use modulo arithmetic on indices to treat a fixed-size array as a ring buffer, achieving true O(1) enqueue/dequeue.
- Linked-list: Maintain pointers to both head and tail of a singly linked list; enqueue at tail and dequeue at head each take O(1).

# Common Applications
- Breadth-first search (BFS): Traverse graphs level by level by enqueuing neighbors.- 
- Buffering & scheduling: Manage print queues, I/O buffers, and task scheduling systems.
- Producer-consumer problems: Synchronize data exchange between threads or processes using a queue as the buffer.
