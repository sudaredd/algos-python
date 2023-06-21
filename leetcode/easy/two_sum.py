from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            dif = target - num
            if dif in dic:
                return [dic[dif], idx]
            dic[num]= idx
        return []


ts = TwoSum()
print(ts.twoSum([2, 7, 11, 15], 9))
print(ts.twoSum([3, 2, 4], 6))
print(ts.twoSum([3, 3], 6))
