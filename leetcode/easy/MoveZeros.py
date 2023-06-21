from typing import List


class MoveZeros:
    def moveZeroes(self, nums: List[int]) -> None:
        """
            Do not return anything, modify nums in-place instead.
            Input: nums = [0,1,0,3,12]
            Output: [1,3,12,0,0]
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos = pos + 1
        while pos < len(nums):
            nums[pos] = 0
            pos = pos + 1


mv = MoveZeros()
nums = [0, 1, 0, 3, 12]
mv.moveZeroes(nums)
print(nums)