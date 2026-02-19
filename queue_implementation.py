"""
queue_implementation.py

This module implements Queue data structures.
"""

from collections import deque

class QueueList:
    """
    Queue implementation using a Python list and two pointers (indices).
    FIFO (First In First Out)
    Note: In a real-world scenario with a list, the memory grows indefinitely
    unless we periodically resize or use a circular buffer. This implementation
    focuses on the two-pointer logic.
    """
    def __init__(self):
        self._items = []
        self._front = 0

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.
        Time Complexity: O(1) (amortized)
        """
        self._items.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.
        Time Complexity: O(1)
        """
        if self.is_empty():
            print("Queue is empty")
            return None

        item = self._items[self._front]
        self._front += 1
        return item

    def front(self):
        """
        Returns the item at the front of the queue without removing it.
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None
        return self._items[self._front]

    def is_empty(self):
        """
        Checks if the queue is empty.
        Time Complexity: O(1)
        """
        return self._front >= len(self._items)

    def size(self):
        """
        Returns the number of items in the queue.
        Time Complexity: O(1)
        """
        return len(self._items) - self._front


class QueueDeque:
    """
    Queue implementation using collections.deque.
    FIFO (First In First Out)
    This is the preferred way to implement a queue in Python.
    """
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.
        Time Complexity: O(1)
        """
        self._items.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.
        Time Complexity: O(1)
        """
        if self.is_empty():
            print("Queue is empty")
            return None
        return self._items.popleft()

    def front(self):
        """
        Returns the item at the front of the queue without removing it.
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        """
        Checks if the queue is empty.
        Time Complexity: O(1)
        """
        return len(self._items) == 0

    def size(self):
        """
        Returns the number of items in the queue.
        Time Complexity: O(1)
        """
        return len(self._items)

if __name__ == "__main__":
    print("=== Queue (List) ===")
    q_list = QueueList()
    q_list.enqueue(1)
    q_list.enqueue(2)
    q_list.enqueue(3)
    print(f"Front: {q_list.front()}")
    print(f"Dequeue: {q_list.dequeue()}")
    print(f"Size: {q_list.size()}")
    print()

    print("=== Queue (Deque) ===")
    q_deque = QueueDeque()
    q_deque.enqueue(1)
    q_deque.enqueue(2)
    q_deque.enqueue(3)
    print(f"Front: {q_deque.front()}")
    print(f"Dequeue: {q_deque.dequeue()}")
    print(f"Size: {q_deque.size()}")
