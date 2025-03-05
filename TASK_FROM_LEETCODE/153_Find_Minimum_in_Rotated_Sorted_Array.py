from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.quick_sort(nums)[0]

    def quick_sort(self, arr):
        if len(arr) < 2:
            return arr

        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greather = [i for i in arr[1:] if i > pivot]

        return self.quick_sort(less) + [pivot] + self.quick_sort(greather)