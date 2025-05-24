from typing import List


class Solution:


    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        mx_area = 0
        while l < r:
            current_area = min(height[l], height[r]) * (r-l)
            mx_area = max(mx_area, current_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return mx_area

s = Solution()
m = s.maxArea([1,8,6,2,5,4,8,3,7])
print(m)