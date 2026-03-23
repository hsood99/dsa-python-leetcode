# Find Pivot Index
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum, left_sum = sum(nums), 0
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if right_sum == left_sum: return i
            left_sum += nums[i] 
        return -1