from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = len(heights)
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                print(i,j)
                if j == 0:
                    ret = max(heights[j], ret)

        return ret


sol = Solution()
print(sol.largestRectangleArea([7,1,7,2,2,4]))
print(sol.largestRectangleArea([1,3,7]))