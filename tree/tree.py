
from collections import deque


class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:

    def build_tree(arr):
        if not arr or arr[0] is None:
            return None

        root = Node(arr[0])
        queue = deque([root])
        i = 1

        while queue and i < len(arr):
            node = queue.popleft()

            if i < len(arr) and arr[i] is not None:
                node.left = Node(arr[i])
                queue.append(node.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                node.right = Node(arr[i])
                queue.append(node.right)
            i += 1

        return root