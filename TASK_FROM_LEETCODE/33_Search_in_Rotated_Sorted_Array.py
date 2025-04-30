from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if len(nums) == 2:
            res = [i for i in range(high+1) if nums[i] == target]
            return res[0] if res else -1
        
        while low <= high:
            mid = (low + high) // 2

            if nums[low] == target: return low
            if nums[mid] == target: return mid
            if nums[high] == target: return high
            if high - mid == mid - low: return -1

            if target < nums[mid] and target < nums[low]:
                high = mid - 1
            elif target < nums[mid] and target > nums[low]:
                low = mid + 1

            print(high, low, mid)

        return -1 
    
s = Solution()
s.search([4,5,6,7,0,1,2], 3)