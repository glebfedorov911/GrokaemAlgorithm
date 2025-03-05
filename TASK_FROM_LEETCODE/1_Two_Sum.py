from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {target-nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            if nums[i] in hash_nums and i != hash_nums[nums[i]]:
                return i, hash_nums[nums[i]]
            

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))