class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = []
        for i in s:
            if i in "([{":
                arr.append(i)
            else:
                if len(arr) < 1:
                    return False
                popped = arr.pop()
                if i == ")":
                    if popped != "(":
                        return False
                elif i == "}":
                    if popped != "{":
                        return False
                else:
                    if popped != "[":
                        return False
        if len(arr) != 0:
            return False
        return True
                
        

sol = Solution()
print(sol.isValid("([[]])"))