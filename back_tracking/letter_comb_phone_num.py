# Letter Combinations of a Phone Number
# Medium
# Topics
# Company Tags
# Hints
# You are given a string digits made up of digits from 2 through 9 inclusive.

# Each digit (not including 1) is mapped to a set of characters as shown below:

# A digit could represent any one of the characters it maps to.

# Return all possible letter combinations that digits could represent. You may return the answer in any order.



# Example 1:

# Input: digits = "34"

# Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
# Example 2:

# Input: digits = ""

# Output: []
# Constraints:

# 0 <= digits.length <= 4
# 2 <= digits[i] <= 9

num_dicts = {
    "1": [],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []

        def backtrack(num_dict):
            nonlocal ret
            if len(ret) == 0:
                ret = num_dict
                return
            
            my_arr = []
            # ret_copy = ret.copy()
            for i in ret:
                for j in num_dict:
                    my_arr.append(i+j)
                  
            ret = my_arr

        
        for i in digits:
            backtrack(num_dicts[i])

        return ret


sol = Solution()
print(sol.letterCombinations("34"))