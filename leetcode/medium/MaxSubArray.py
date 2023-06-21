from typing import List
import sys

class MaxSubArray:
    """
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    """

    def maxSubArray(self, nums: List[int]) -> int:
        mx = -sys.maxsize
        total = 0
        for num in nums:
            total += num
            mx = max(mx, total)
            if total < 0:
                total = 0
        return mx


mx = MaxSubArray()
print(mx.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
