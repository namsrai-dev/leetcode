# Word Search
# Medium
# Topics
# Company Tags
# Hints
# Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

# For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

# Example 1:



# Input: 
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "CAT"

# Output: true
# Example 2:



# Input: 
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "BAT"

# Output: false


# iterate through each of item.    A -> B -> C -> D -> S -> A ...
# [A,B], [A,C] || [A,B] ->  [A,B,C], [A,B,A]

# edge cases: should not go back, if len(col) == len(word) no need to go more 



from typing import List


# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         ret = False

#         def backtrack(idx_i, idx_j, count, letter, dir=None):
#             nonlocal ret
#             if letter == word:
#                 # print("word found !!!")
#                 ret = True
#                 return
#             elif count == len(word):
#                 # print("word could not found !!!", letter)
#                 return
            
#             # go right if possible
#             if idx_j + 1 < len(board[idx_i]) and dir != "left":
#                 backtrack(idx_i, idx_j+1, count+1, letter+board[idx_i][idx_j+1], "right")

#             # go left if possible
#             if idx_j - 1 >= 0 and dir != "right":
#                 # print("check", idx_i, idx_j)
#                 backtrack(idx_i, idx_j-1, count+1, letter+board[idx_i][idx_j-1], "left")

#             # go up if possible
#             if idx_i - 1 >= 0 and dir != "down":
#                 backtrack(idx_i - 1, idx_j, count+1, letter+board[idx_i-1][idx_j], "up")

#             # # go down if possible
#             if idx_i + 1 < len(board) and dir != "down":
#                 # print("len board",len(board))
#                 backtrack(idx_i + 1, idx_j, count+1, letter+board[idx_i+1][idx_j], "up")




#         for idx_i, i  in enumerate(board):
#             for idx_j, j  in enumerate(i):
#                 # print()
#                 backtrack(idx_i, idx_j, 1, j)

#         return ret

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or visited[r][c]):
                return False

            visited[r][c] = True
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            visited[r][c] = False
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


sol = Solution()

# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ]

# word = "CAT"

board=[["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
word="aaaaaaaaaaaaa"

print(sol.exist(board, word))