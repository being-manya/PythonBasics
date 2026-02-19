"""
stack.py

This module implements a Stack data structure.
"""

class Stack:
    """
    Stack implementation using a Python list internally.
    LIFO (Last In First Out)
    """
    def __init__(self):
        self._items = []

    def push(self, item):
        """
        Adds an item to the top of the stack.
        Time Complexity: O(1) (amortized)
        """
        self._items.append(item)

    def pop(self):
        """
        Removes and returns the item from the top of the stack.
        Time Complexity: O(1)
        """
        if self.is_empty():
            print("Stack is empty")
            return None
        return self._items.pop()

    def peek(self):
        """
        Returns the item at the top of the stack without removing it.
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        """
        Checks if the stack is empty.
        Time Complexity: O(1)
        """
        return len(self._items) == 0

    def size(self):
        """
        Returns the number of items in the stack.
        Time Complexity: O(1)
        """
        return len(self._items)

if __name__ == "__main__":
    print("=== Stack ===")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Peek: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"Size: {stack.size()}")
    print(f"Is Empty: {stack.is_empty()}")
