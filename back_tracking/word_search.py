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


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


sol = Solution()

board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],

word = "CAT"

sol.exist(board, word)