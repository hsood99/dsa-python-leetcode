# Maximum Subarray
# Approach 1 
# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         running_sum, max_sum, min_prefix = 0, float('-inf'), 0
#         for num in nums:
#             running_sum += num
#             max_sum = max_sum if max_sum > running_sum - min_prefix else running_sum - min_prefix
#             min_prefix = min_prefix if min_prefix < running_sum else running_sum

#         return max_sum


# Approach 2 (kadane)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = cur_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max_sum if max_sum > cur_sum else cur_sum
        return max_sum