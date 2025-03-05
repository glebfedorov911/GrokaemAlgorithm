from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        nums_odd_idx = [nums[i] for i in range(1, len(nums), 2)]
        nums_even_idx = [nums[i] for i in range(0, len(nums), 2)]
        
        nums_odd_idx.sort(key=lambda x: x, reverse=True)
        nums_even_idx.sort(key=lambda x: x, reverse=False)
        
        results = []
        mx = max(len(nums_even_idx), len(nums_odd_idx))
        for i in range(mx):
            if i < len(nums_even_idx):
                results.append(nums_even_idx[i])
            if i < len(nums_odd_idx):
                results.append(nums_odd_idx[i])

        return results

s = Solution()
print(
    s.sortEvenOdd([5,39,33,5,12,27,20,45,14,25,32,33,30,30,9,14,44,15,21])
)