# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root and (root.left or root.right):
            left = root.left
            right = root.right
            root.left = right
            root.right = left
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            # if root.left and root.right:
                # root.left = right
                # root.right = left
                # self.invertTree(root.left)
                # self.invertTree(root.right)
        
        # elif root and root.left



        return root