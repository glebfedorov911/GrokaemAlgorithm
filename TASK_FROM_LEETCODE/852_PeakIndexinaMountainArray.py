class Solution:
    def peakIndexInMountainArray(self, arr):
        return self.binary_mountain_search(arr)

    @staticmethod
    def binary_mountain_search(n):
        low = 0
        high = len(n) - 1

        while low < high:
            mid = (low + high) // 2

            if n[mid] > n[mid+1]:
                high = mid
            else:
                low = mid + 1

        return max(low, high)
