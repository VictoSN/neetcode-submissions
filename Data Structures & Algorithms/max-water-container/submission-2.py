class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_highest = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if min(heights[i], heights[j]) * abs(i - j) > current_highest:
                    current_highest = min(heights[i], heights[j]) * abs(i - j)

        return current_highest