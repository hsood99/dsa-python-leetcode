# Continuous Subarray Sum

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        hmap, prefix = {0: -1}, 0
        for i in range(len(nums)):
            prefix += nums[i]
            mod = prefix % k
            if mod in hmap:
                if i - hmap[mod] >= 2:
                    return True
            else:
                hmap[mod] = i
        return False