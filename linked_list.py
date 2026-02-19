"""
linked_list.py

This module implements a custom Singly Linked List.
"""

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

if __name__ == "__main__":
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

    if ll.head and ll.head.next and ll.head.next.next and ll.head.next.next.next:
        node30 = ll.head.next.next.next
        node20 = ll.head.next
        node30.next = node20 # Cycle created: 30 -> 20

        print(f"Cycle Detected: {ll.detect_cycle() is not None}")

        ll.remove_cycle()
        print(f"Cycle Detected after removal: {ll.detect_cycle() is not None}")
        print("Traverse after cycle removal:")
        ll.traverse()
