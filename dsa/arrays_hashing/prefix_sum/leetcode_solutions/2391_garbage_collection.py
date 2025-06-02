# Leetcode 2391. Minimum Amount of Time to Collect Garbage
# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_time = 0

        # Precompute travel prefix sum
        prefix = [0] * len(garbage)
        for i in range(1, len(garbage)):
            prefix[i] = prefix[i - 1] + travel[i - 1]

        # Track last index and count of each garbage type
        last_index = {'M': 0, 'P': 0, 'G': 0}
        count = {'M': 0, 'P': 0, 'G': 0}

        for i, g in enumerate(garbage):
            for ch in g:
                count[ch] += 1
                last_index[ch] = i

        # Compute total time for each garbage type
        for ch in 'MPG':
            total_time += count[ch]         # pickup time
            total_time += prefix[last_index[ch]]  # travel time

        return total_time
