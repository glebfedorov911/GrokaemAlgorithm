def isBadVersion(version):
    '''solve already in leetcode'''
    ...

class Solution:
    def firstBadVersion(self, n):
        return self.binary_search_bad_version(n)

    @staticmethod
    def binary_search_bad_version(n):
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            guess = mid+1

            if isBadVersion(guess):
                high = mid - 1
            else:
                low = mid + 1

        return max(low, high) + 1