"""
strings.py

This module implements fundamental string algorithms.
"""

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
