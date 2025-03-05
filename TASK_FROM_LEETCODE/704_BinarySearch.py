class Solution:
    
    def search(self, nums, target):
        return self.binary_search_algorithm(nums=nums, target=target)

    @staticmethod
    def binary_search_algorithm(nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if guess == target:
                return mid
            elif guess > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1