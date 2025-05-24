from typing import  List


class Solution:


    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        while k < len(nums):
            if nums.count(nums[k]) > 1:
                nums.pop(k)
            else:
                k += 1

        return k

s = Solution()
r = s.removeDuplicates([1, 2])
print(r)