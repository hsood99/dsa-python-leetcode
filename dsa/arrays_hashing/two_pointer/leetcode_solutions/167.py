# 167. Two Sum II - Input Array Is Sorted
"""
🔶 Problem Statement:
You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, and an integer target. Return the indices of the two numbers such that they add up to target.

You must return the answer as an array of the two indices (1-based).

Use only constant extra space.

🔍 Step-by-Step Thinking:
Array is sorted ➝ 🔑 Use two pointers.

Set left = 0, right = len(numbers) - 1

While left < right:

Calculate sum = numbers[left] + numbers[right]

If sum == target: ✅ return [left + 1, right + 1]

If sum < target: ➝ Move left forward.

If sum > target: ➝ Move right backward.
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            if total < target:
                left += 1
            else:
                right -= 1