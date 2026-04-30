# K Closest Points to Origin
# Medium
# Topics
# Company Tags
# Hints
# You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

# Return the k closest points to the origin (0, 0).

# The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

# You may return the answer in any order.

# Example 1:



# Input: points = [[0,2],[2,2]], k = 1

# Output: [[0,2]]
# Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

# Example 2:

# Input: points = [[0,2],[2,0],[2,2]], k = 2

# Output: [[0,2],[2,0]]
# Explanation: The output [2,0],[0,2] would also be accepted.

# Constraints:

# 1 <= k <= points.length <= 1000
# -100 <= points[i][0], points[i][1] <= 100

import heapq
import math
from typing import List


class Solution:

    def get_distance(self, points: List) -> int:
        x, y = points[0], points[1]
        distance = (math.sqrt((math.pow(x, 2) + math.pow(y, 2))))
        return distance

    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        min_heap = []
        for arr in points:
            dist = self.get_distance(arr)
            dist = self.get_distance(arr)
            min_heap.append([dist, arr[0], arr[1]])

        heapq.heapify(min_heap)

        while k > 0:
            popped = heapq.heappop(min_heap)
            res.append([popped[1],popped[2]])
            k = k - 1


        return res




sol = Solution()
print(sol.kClosest([[0,2],[2,0],[2,2]], 2))
