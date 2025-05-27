class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_map = {0: 1}
        prefix = 0
        for num in nums:
            prefix += num
            diff = prefix - k
            if diff in prefix_map:
                count += prefix_map[diff]
            prefix_map[prefix] = prefix_map.get(prefix, 0) + 1
        return count