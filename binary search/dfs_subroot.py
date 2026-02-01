# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkEqual(root1, root2):
            if root1.left and root2.left:
                if checkEqual(root1.left, root2.left) is False:
                    return False
            elif root1.left or root2.left:
                return False

            if root1.right and root2.right:
                if checkEqual(root1.right, root2.right) is False:
                    return False
            elif root1.right or root2.right:
                return False

            if root1.val != root2.val:
                return False

        def dfs(root):
            if root.left:
                if dfs(root.left):
                    return True
            if root.right:
                if dfs(root.right):
                    return True

            if root.val == subRoot.val:
               if checkEqual(root, subRoot) != False:
                # print("return true")
                return True

        if root:
            ret = dfs(root)
            if ret is None:
                return False
            return ret

        return False