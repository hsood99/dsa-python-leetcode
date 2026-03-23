# Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """This functions returns running sum"""
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        
        return nums