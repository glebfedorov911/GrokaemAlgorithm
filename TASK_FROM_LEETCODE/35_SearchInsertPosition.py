class Solution(object):
    def searchInsert(self, nums, target):
        return self.binary_search_insert(nums, target)

    @staticmethod
    def binary_search_insert(nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if target == guess:
                return mid
            elif guess > target:
                high = mid - 1
            else:
                low = mid + 1 

        return low