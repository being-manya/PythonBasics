"""
binary_tree.py

This module implements Binary Tree traversals.
"""

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
    print("=== Binary Tree ===")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(f"Inorder: {inorder_traversal(root)}")
    print(f"Preorder: {preorder_traversal(root)}")
    print(f"Postorder: {postorder_traversal(root)}")
