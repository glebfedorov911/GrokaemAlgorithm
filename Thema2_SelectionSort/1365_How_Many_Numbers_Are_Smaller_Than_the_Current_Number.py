from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sorted(nums).index(i) for i in nums]

    def _selection_sort(self, nums):
        copy_nums = nums.copy()
        sorted_array = []

        for _ in range(len(copy_nums)):
            sm = copy_nums.pop(self._find_smallest(copy_nums))
            sorted_array.append(sm)

        return sorted_array

    def _find_smallest(self, nums):
        smallest_index = 0

        for i in range(len(nums)):
            if nums[i] < nums[smallest_index]:
                smallest_index = i

        return smallest_index