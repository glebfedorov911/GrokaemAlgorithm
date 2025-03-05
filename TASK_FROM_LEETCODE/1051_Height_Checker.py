class Solution():


    def heightChecker(self, heights):
        return self._selection_sort_count_not_same_place(heights)

    def _selection_sort_count_not_same_place(self, heights):
        heights_copy = heights.copy()
        now_idx = 0
        count = 0

        while heights_copy:
            num_idx = self._findest_smallest_idx(heights_copy)
            num = heights_copy.pop(num_idx)

            if num != heights[now_idx]:
                count += 1
            
            now_idx += 1

        return count

    def _findest_smallest_idx(self, heights):
        smallest_idx = 0
        smallest = heights[smallest_idx]

        for i in range(len(heights)):
            if heights[i] < smallest:
                smallest_idx = i
                smallest = heights[smallest_idx]
        
        return smallest_idx

s = Solution()

print(
    s.heightChecker([5,1,2,3,4])
)