# Range Sum query

class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    
    def sumRange(self, left: int, right: int) -> int:
        """
        Computes sum range using formula prefix[right + 1] - prefix[left - 1]
        
        Note:
            This function modifies the input list in-place.

        Args:
            left: Starting index from where we need to compute sum.
            right: Index until which sum will be computed

        Returns:
            Sum range from left to right
        """
        return self.prefix[right + 1] - self.prefix[left]