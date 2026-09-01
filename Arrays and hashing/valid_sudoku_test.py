# Valid Sudoku
# Medium
# Topics
# Company Tags
# Hints
# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Example 1:



# Input: board =
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true
# Example 2:

# Input: board =
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: false
# Explanation: There are two 1's in the top-left 3x3 sub-box.

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.



from rpds import List


from typing import List

# [0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [0,7], [0,8]
# [1,0], [1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8]
# [2,0], [2,1], [2,2], [2,3], [2,4], [2,5], [2,6], [2,7], [2,8]
# [3,0], [3,1], [3,2], [3,3], [3,4], [3,5], [3,6], [3,7], [3,8]
# [4,0], [4,1], [4,2], [4,3], [4,4], [4,5], [4,6], [4,7], [4,8]
# [5,0], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6], [5,7], [5,8]

board1 = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
]

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ret = True

        for i in board:
            if self.hasDuplicate(i):
                ret = False
        arr2 = [
            [[],[],[]],
            [[],[],[]],
            [[],[],[]]
        ]
        for i in range(len(board)):
            my_arr = []
            for j in range(len(board[0])):
                arr2[i//3][j//3].append(board[i][j])
                my_arr.append(board[j][i])
            if self.hasDuplicate(my_arr):
                ret = False


        for row in arr2:
            for col in row:
                if self.hasDuplicate(col):
                    ret = False
        return ret

    def hasDuplicate(self, i: List[str]) -> bool:
        char_list = [char for char in i if char != '.']
        return len(char_list) != len(set(char_list))


sol = Solution()
print(sol.isValidSudoku(board1))
