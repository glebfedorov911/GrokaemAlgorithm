class Solution(object):
    
    
    def shuffle(self, nums, n):
        nums1 = nums[:n]
        nums2 = nums[n:]

        return self._shuffle(nums1, nums2)

    @staticmethod
    def _shuffle(nums1, nums2):
        nums = zip(nums1, nums2)
        result = []

        for i, j in nums:
            result.append(i)
            result.append(j)

        return result