# 125. Valid Palindrome
"""
🔶 Description:
Given a string s, return true if it is a palindrome, considering only alphanumeric characters and ignoring cases.
example:
Input:  "A man, a plan, a canal: Panama"
Output: true

Explanation: "amanaplanacanalpanama" is a palindrome

🧠 Step-by-Step Plan (Two Pointers):
✅ What we need:
Ignore non-alphanumeric characters.

Convert all characters to lowercase.

Use two pointers: one starting from the beginning, one from the end.

If characters match, move inward.

If mismatch → return False.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = [char.lower() for char in s if char.isalnum()]
        left, right = 0, len(c) - 1
        while left < right:
            if c[left] != c[right]:
                return False
            left += 1
            right -= 1
        return True