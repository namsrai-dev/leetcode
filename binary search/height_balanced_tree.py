from typing import Optional

# 1. The TreeNode class definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            
            # A node is balanced if:
            # 1. Left subtree is balanced
            # 2. Right subtree is balanced
            # 3. Height difference is <= 1
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

# --- TEST CASE ---

# We will build an UNBALANCED tree:
#        1
#       / \
#      2   3
#     /
#    4
#   /˜
#  5 (This makes it unbalanced because the left side is height 4, right is 2)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)

sol = Solution()
result = sol.isBalanced(root)

print(f"Is the tree balanced? {result}")