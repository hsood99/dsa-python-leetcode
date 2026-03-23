# Binary Subarrays With Sum
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        result, running_sum, hmap = 0, 0, {0: 1}
        for num in nums:
            running_sum += num
            if running_sum - goal in hmap:
                result += hmap[running_sum - goal]
            
            hmap[running_sum] = hmap.get(running_sum, 0) + 1
        return result