# Intervals Between Identical Elements
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        hmap, res = {}, [0] * len(arr)
        for i, val in enumerate(arr):
            lst = hmap.get(val, [])
            lst.append(i)
            hmap[val] = lst
        for val in hmap:
            indices = hmap[val]
            prefix = [0] * len(indices)
            prefix[0] = indices[0]
            for i in range(1, len(indices)):
                prefix[i] = prefix[i - 1] + indices[i]
            for k, idx in enumerate(indices):
                left = idx * k - (prefix[k-1] if k > 0 else 0)
                right = (prefix[-1] - prefix[k]) - idx * (len(indices) - k - 1)
                res[idx] = left + right

            # print(res)
        return res
