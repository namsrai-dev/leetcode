# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.



# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.90
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

def get_first_digit(value):
    return int(str(value)[0])

def hasNext(value, value2):
    ret = False
    if value -1 > value2:
        ret = True
    return ret

class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        convert = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        i = 0
        num = 0
        while i < len(s):
            if hasNext(len(s), i):
                num1 = convert[s[i]]
                num2 = convert[s[i+1]]
                if num1 < num2 and num2 / num1 == 10:
                    i += 1
                    num += num2-num1
                elif num1 == num2 and get_first_digit(num1) == 1:
                    i = i+1
                    if hasNext(len(s), i):
                        num3 = convert[s[i+1]]
                        if num2 == num3:
                            i = i+1
                            num += num3 * 3
                        else:
                            num += num2*2
                    else:
                        num += num2*2

                elif num1 < num2 and num2 / num1 == 5:
                    i += 1
                    num += num2-num1
                else:
                    num += convert[s[i]]
            else:
                num += convert[s[i]]
            i += 1
        print(num)
        return num

Solution().romanToInt("LVIII")
