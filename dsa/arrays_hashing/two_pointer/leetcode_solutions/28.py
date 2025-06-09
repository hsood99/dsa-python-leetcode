# 28. Find the Index of the First Occurrence in a String
"""
Here:

i moves across the haystack

j checks each character of needle using a pointer comparison

This mimics the Two Pointers concept explicitly.
"""

# Brute force approach
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         for i in range(len(haystack) - len(needle) + 1):
#             if haystack[i:i + len(needle)] == needle:
#                 return i
#         return -1

# two pointer appraoch
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        if m == 0:
            return 0

        for i in range(n - m + 1):
            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            if j == m:
                return i

        return -1
