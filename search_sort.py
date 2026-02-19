"""
search_sort.py

This module implements basic Searching and Sorting algorithms.
"""

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

if __name__ == "__main__":
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
