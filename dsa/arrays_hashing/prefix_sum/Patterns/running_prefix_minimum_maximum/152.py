# Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_prod = cur_max = cur_min = nums[0]
        for i in range(1, len(nums)):
            temp_max = cur_max
            cur_max = max(nums[i], nums[i] * cur_max, nums[i] * cur_min)
            cur_min = min(nums[i], nums[i] * temp_max, nums[i] * cur_min)
            max_prod = max_prod if max_prod > cur_max else cur_max
        return max_prod
