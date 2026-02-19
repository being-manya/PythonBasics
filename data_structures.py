"""
data_structures.py

This module implements fundamental data structures and algorithms in Python.
It is designed for interview preparation and includes:
1. String Algorithms
2. Singly Linked List (Custom Implementation)
3. Stack Implementation
4. Queue Implementation
5. Search & Sort Algorithms
6. Binary Tree Traversal

Author: Jules
"""

# ==========================================
# 1. String Algorithms
# ==========================================

def traverse_string(s):
    """
    Traverses the string and prints characters one by one.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if s is None:
        return
    for char in s:
        print(char)

def reverse_string(s):
    """
    Reverses the string using loops.

    Time Complexity: O(n)
    Space Complexity: O(n) (strings are immutable in Python)
    """
    if s is None:
        return None
    reversed_chars = []
    for i in range(len(s) - 1, -1, -1):
        reversed_chars.append(s[i])
    return "".join(reversed_chars)

def is_palindrome(s):
    """
    Checks if a string is a palindrome.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if s is None:
        return False
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def count_vowels_consonants(s):
    """
    Counts vowels and consonants in a string.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if s is None:
        return 0, 0
    vowels = set("aeiouAEIOU")
    v_count = 0
    c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

def char_frequency(s):
    """
    Returns a dictionary of character frequencies.

    Time Complexity: O(n)
    Space Complexity: O(k) where k is the number of unique characters
    """
    if s is None:
        return {}
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def first_non_repeating_char(s):
    """
    Returns the first non-repeating character in the string.

    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    if s is None:
        return None
    freq = char_frequency(s)
    for char in s:
        if freq[char] == 1:
            return char
    return None

def remove_duplicates(s):
    """
    Removes duplicate characters while maintaining order.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if s is None:
        return None
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)

# ==========================================
# 2. Singly Linked List (Custom Implementation)
# ==========================================

class Node:
    """
    Node class for Singly Linked List.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Singly Linked List implementation.
    """
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """
        Inserts a new node at the beginning of the list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Inserts a new node at the end of the list.
        Time Complexity: O(n)
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, pos, data):
        """
        Inserts a new node at the specified position (0-indexed).
        Time Complexity: O(n)
        """
        if pos < 0:
            print("Invalid position")
            return

        if pos == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0

        while current and count < pos - 1:
            current = current.next
            count += 1

        if not current:
            print("Position out of bounds")
            return

        new_node.next = current.next
        current.next = new_node

    def delete_by_value(self, val):
        """
        Deletes the first occurrence of a node with the given value.
        Time Complexity: O(n)
        """
        if not self.head:
            return

        if self.head.data == val:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != val:
            current = current.next

        if current.next:
            current.next = current.next.next

    def delete_at_position(self, pos):
        """
        Deletes the node at the specified position (0-indexed).
        Time Complexity: O(n)
        """
        if not self.head or pos < 0:
            return

        if pos == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0
        while current.next and count < pos - 1:
            current = current.next
            count += 1

        if not current.next:
            return

        current.next = current.next.next

    def search(self, val):
        """
        Searches for a value in the list. Returns True if found, False otherwise.
        Time Complexity: O(n)
        """
        current = self.head
        while current:
            if current.data == val:
                return True
            current = current.next
        return False

    def traverse(self):
        """
        Prints the elements of the list.
        Time Complexity: O(n)
        """
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def length(self):
        """
        Returns the number of nodes in the list.
        Time Complexity: O(n)
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse_iterative(self):
        """
        Reverses the linked list iteratively.
        Time Complexity: O(n)
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def reverse_recursive(self):
        """
        Reverses the linked list recursively.
        Time Complexity: O(n)
        """
        def _reverse(current, prev):
            if not current:
                return prev
            next_node = current.next
            current.next = prev
            return _reverse(next_node, current)

        self.head = _reverse(self.head, None)

    def middle_element(self):
        """
        Returns the middle element of the list.
        Time Complexity: O(n)
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def detect_cycle(self):
        """
        Detects if there is a cycle in the list using Floyd's Cycle-Finding Algorithm.
        Returns the node where the cycle begins (technically the meeting point inside cycle) if found, else None.
        Wait, standard Floyd's returns meeting point. To find start, we need extra steps.
        This function just returns the meeting point node if cycle exists, or None.
        Time Complexity: O(n)
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None

    def remove_cycle(self):
        """
        Detects and removes a cycle in the linked list.
        Time Complexity: O(n)
        """
        # 1. Detect cycle
        slow = self.head
        fast = self.head
        cycle_detected = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle_detected = True
                break

        if not cycle_detected:
            return

        # 2. Find start of cycle
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        start_of_cycle = slow

        # 3. Remove cycle
        # Find the last node in the cycle (node pointing to start_of_cycle)
        current = start_of_cycle
        while current.next != start_of_cycle:
            current = current.next

        current.next = None

# ==========================================
# 3. Stack Implementation
# ==========================================

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

# ==========================================
# 4. Queue Implementation
# ==========================================

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

# ==========================================
# 5. Search & Sort Algorithms
# ==========================================

def binary_search_iterative(arr, target):
    """
    Performs binary search iteratively.
    Assumes arr is sorted.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(arr, target, left, right):
    """
    Performs binary search recursively.
    Assumes arr is sorted.
    Time Complexity: O(log n)
    Space Complexity: O(log n) (recursion stack)
    """
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

def bubble_sort(arr):
    """
    Sorts the array using Bubble Sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    """
    Sorts the array using Selection Sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """
    Sorts the array using Insertion Sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# ==========================================
# 6. Binary Tree Traversal
# ==========================================

class TreeNode:
    """
    Node class for Binary Tree.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root):
    """
    Performs Inorder Traversal (Left, Root, Right).
    Time Complexity: O(n)
    """
    res = []
    if root:
        res = inorder_traversal(root.left)
        res.append(root.data)
        res = res + inorder_traversal(root.right)
    return res

def preorder_traversal(root):
    """
    Performs Preorder Traversal (Root, Left, Right).
    Time Complexity: O(n)
    """
    res = []
    if root:
        res.append(root.data)
        res = res + preorder_traversal(root.left)
        res = res + preorder_traversal(root.right)
    return res

def postorder_traversal(root):
    """
    Performs Postorder Traversal (Left, Right, Root).
    Time Complexity: O(n)
    """
    res = []
    if root:
        res = postorder_traversal(root.left)
        res = res + postorder_traversal(root.right)
        res.append(root.data)
    return res

if __name__ == "__main__":
    print("=== String Algorithms ===")
    s = "hello world"
    print(f"Original: {s}")
    traverse_string(s)
    print(f"Reversed: {reverse_string(s)}")
    print(f"Is Palindrome ('racecar'): {is_palindrome('racecar')}")
    print(f"Is Palindrome ('hello'): {is_palindrome('hello')}")
    print(f"Vowels/Consonants: {count_vowels_consonants(s)}")
    print(f"Frequency: {char_frequency(s)}")
    print(f"First Non-Repeating: {first_non_repeating_char('swiss')}")
    print(f"Remove Duplicates: {remove_duplicates('banana')}")
    print()

    print("=== Linked List ===")
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.insert_at_position(2, 15) # 5 -> 10 -> 15 -> 20
    print("Traverse:")
    ll.traverse()
    print(f"Length: {ll.length()}")
    print(f"Search 15: {ll.search(15)}")
    print(f"Search 100: {ll.search(100)}")

    ll.delete_by_value(10) # 5 -> 15 -> 20
    print("After delete 10:")
    ll.traverse()

    ll.delete_at_position(0) # 15 -> 20
    print("After delete at pos 0:")
    ll.traverse()

    ll.insert_at_end(25)
    ll.insert_at_end(30) # 15 -> 20 -> 25 -> 30
    print("Before Reverse:")
    ll.traverse()

    ll.reverse_iterative()
    print("After Reverse Iterative:")
    ll.traverse()

    ll.reverse_recursive()
    print("After Reverse Recursive:")
    ll.traverse()

    print(f"Middle Element: {ll.middle_element()}")

    # Cycle detection
    # Create a cycle for testing: 30 -> 25 -> 20 -> 15 -> 25...
    # head is 30. next is 25. next is 20. next is 15.
    # 30 -> 25 -> 20 -> 15 -> None
    # Let's make 15 point to 25 (the second node)
    # 15 is ll.head.next.next.next
    # 25 is ll.head.next

    # But currently list is reversed back to original? No.
    # Initial: 5 -> 10 -> 15 -> 20
    # Ops: delete 10 -> 5 -> 15 -> 20
    # Ops: delete pos 0 -> 15 -> 20
    # Ops: append 25, 30 -> 15 -> 20 -> 25 -> 30
    # Reverse Iterative -> 30 -> 25 -> 20 -> 15
    # Reverse Recursive -> 15 -> 20 -> 25 -> 30

    # So list is 15 -> 20 -> 25 -> 30
    # But wait, 15 is head.

    if ll.head and ll.head.next and ll.head.next.next and ll.head.next.next.next:
        node30 = ll.head.next.next.next
        node20 = ll.head.next
        node30.next = node20 # Cycle created: 30 -> 20

        print(f"Cycle Detected: {ll.detect_cycle() is not None}")

        ll.remove_cycle()
        print(f"Cycle Detected after removal: {ll.detect_cycle() is not None}")
        print("Traverse after cycle removal:")
        ll.traverse()
    print()

    print("=== Stack ===")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Peek: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"Size: {stack.size()}")
    print(f"Is Empty: {stack.is_empty()}")
    print()

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
    print()

    print("=== Search & Sort ===")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr}")
    print(f"Bubble Sort: {bubble_sort(arr.copy())}")
    print(f"Selection Sort: {selection_sort(arr.copy())}")
    print(f"Insertion Sort: {insertion_sort(arr.copy())}")

    sorted_arr = sorted(arr)
    print(f"Sorted for Search: {sorted_arr}")
    print(f"Binary Search (Iterative) for 22: {binary_search_iterative(sorted_arr, 22)}")
    print(f"Binary Search (Recursive) for 22: {binary_search_recursive(sorted_arr, 22, 0, len(sorted_arr)-1)}")
    print(f"Binary Search for 99: {binary_search_iterative(sorted_arr, 99)}")
    print()

    print("=== Binary Tree ===")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(f"Inorder: {inorder_traversal(root)}")
    print(f"Preorder: {preorder_traversal(root)}")
    print(f"Postorder: {postorder_traversal(root)}")
