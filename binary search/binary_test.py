from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1 = 0
        r1 = len(matrix) - 1
        count1 = 0

        while l1 <= r1:
            count1 += 1
            median1 = (l1 + r1) // 2
            if matrix[median1][0] <= target and matrix[median1][-1] >= target:
                my_arr = matrix[median1]
                l2 = 0
                r2 = len(my_arr) - 1
                count2 = 0
                while l2 <= r2:
                    count2 +=1
                    median2 = (l2 + r2) // 2
                    if my_arr[median2] == target:
                        return True
                    elif my_arr[median2] < target:
                        l2 = median2 + 1
                    else:
                        r2 = median2 - 1

                return False

            elif matrix[median1][0] < target:
                l1 = median1 + 1
            else:
                r1 = median1 - 1


        return False





sol = Solution()
print(sol.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10))
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))