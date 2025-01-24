# Input:  s = “ABC”
# Output: “ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”


# Input: s = “XY”
# Output: “XY”, “YX”


# Input: s = “AAA”
# Output: “AAA”, “AAA”, “AAA”, “AAA”, “AAA”, “AAA”

class Solution(object):
    def permitationsOfString(self, strings):
        results = []
        def backtrack(i, curStr):
            if len(curStr) == len(strings):
                results.append(curStr)
                return

            for c in strings:
                print(c, curStr)
                if c not in curStr:
                    backtrack(i+1, curStr+c)

        if strings:
            backtrack(0, "")

        return results


solution = Solution()
print(solution.permitationsOfString("ABC"))