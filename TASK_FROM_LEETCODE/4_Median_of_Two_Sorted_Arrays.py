from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        sorted_nums = self.quick_sort(nums)

        if (ln := len(sorted_nums)) % 2 != 0:
            return float(sorted_nums[ln // 2])
        else:
            return float((sorted_nums[ln // 2 - 1] + sorted_nums[ln // 2]) / 2)

    def quick_sort(self, arr: List[int]):
        if len(arr) < 2:
            return arr
        
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greather = [i for i in arr[1:] if i > pivot]

        return self.quick_sort(less) + [pivot] + self.quick_sort(greather)