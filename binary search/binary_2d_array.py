class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix)
        m = l + (r - l) // 2
        while l < r:
            m = l + (r - l) // 2
            min_mat = matrix[m][0]
            max_mat = matrix[m][len(matrix[m]) - 1]
            if target >= min_mat and target <= max_mat:
                my_arr = matrix[m]
                l2, r2 = 0, len(matrix[m])
                while l2 < r2:
                    m2 = (r2 - l2) // 2 + l2
                    if target == my_arr[m2]:
                        return True
                    elif target > my_arr[m2]:
                        l2 = m2 + 1
                    else:
                        r2 = m2
                return False
            elif target < min_mat:
                r = m
            else:
                l = m + 1
        return False

sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))