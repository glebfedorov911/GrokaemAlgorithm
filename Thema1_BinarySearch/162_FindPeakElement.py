class Solution:
    
    
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 1 if nums[0] < nums[1] else 0

        low = 0
        high = len(nums) - 1
        mid = (low+high) // 2

        while low <= high:

            left_otr = nums[mid-1] if mid-1 >= 0 else -float('inf')
            right_otr = nums[mid+1] if mid+1 < len(nums) else -float('inf')
            
            if left_otr < nums[mid] > right_otr:
                return mid
            elif left_otr < nums[mid] < right_otr:
                low = mid + 1
            elif left_otr > nums[mid] > right_otr:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low+high) // 2


s = Solution()
print(
    s.findPeakElement([3, 2, 1])
)