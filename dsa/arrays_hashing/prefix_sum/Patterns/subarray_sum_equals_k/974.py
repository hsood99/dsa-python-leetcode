# Subarray Sums Divisible by K
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        hmap, result, prefix = {0:1}, 0, 0
        for num in nums:
            prefix += num
            if prefix % k in hmap:
                result += hmap[prefix % k]
            hmap[prefix%k] = hmap.get((prefix % k), 0) + 1
        return result