# Input:  s = “ABC”
# Output: “ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”


# Input: s = “XY”
# Output: “XY”, “YX”


# Input: s = “AAA”
# Output: “AAA”, “AAA”, “AAA”, “AAA”, “AAA”, “AAA”

class Solution(object):
    def permutationsOfString(self, strings):
        results = []
        def backtrack(i, curStr):
            if len(curStr) == len(strings):
                print("push hiigdle", curStr)
                results.append(curStr)
                return

            for c in strings:
                if c not in curStr:
                    print(c, curStr)
                    backtrack(i+1, curStr+c)

        if strings:
            backtrack(0, "")

        return results


solution = Solution()
print(solution.permutationsOfString("ABC"))