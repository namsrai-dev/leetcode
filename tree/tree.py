
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:

    def is_balanced(self, root: Optional[Node]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            print("root value ->",root.val)            
            left_node = dfs(root.left)
            right_node = dfs(root.right)
            print("here the check", root.val, [abs(left_node[1] - right_node[1]) <= 1, max(left_node[1], right_node[1]) + 1])
            if left_node[0] == False or right_node[0] == False:
                return[False, max(left_node[1], right_node[1]) + 1]

            return [abs(left_node[1] - right_node[1]) <= 1, max(left_node[1], right_node[1]) + 1]

        return dfs(root)[0]


    def build_tree(self, arr):
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

    def print_tree(self, root):
        if root is None:
            print("(empty tree)")
            return

        def build(node):
            """Return (lines, mid): equal-width lines and the column of the root's label."""
            label = str(node.val)
            L = build(node.left) if node.left else None
            R = build(node.right) if node.right else None
            if not L and not R:
                return [label], len(label) // 2

            lw = len(L[0][0]) if L else 0
            rw = len(R[0][0]) if R else 0
            gap = 3 if L and R else 0
            r_off = lw + gap                        # where the right block starts
            l_mid = L[1] if L else None
            r_mid = r_off + R[1] if R else None

            if L and R:
                mid = (l_mid + r_mid) // 2          # centre parent between children
            elif L:
                mid = l_mid + 2                     # parent sits up and to the right
            else:
                mid = r_mid - 2                     # parent sits up and to the left

            start = mid - len(label) // 2
            shift = max(0, -start)                  # push everything right if needed
            width = shift + max(start + len(label), r_off + rw)

            top = [" "] * width
            branch = [" "] * width
            top[shift + start : shift + start + len(label)] = label
            if L:
                branch[shift + l_mid + 1] = "/"
                for c in range(l_mid + 2, start):
                    top[shift + c] = "_"
            if R:
                branch[shift + r_mid - 1] = "\\"
                for c in range(start + len(label), r_mid - 1):
                    top[shift + c] = "_"

            lines = ["".join(top), "".join(branch)]
            l_lines = L[0] if L else []
            r_lines = R[0] if R else []
            for i in range(max(len(l_lines), len(r_lines))):
                left_part = l_lines[i] if i < len(l_lines) else " " * lw
                right_part = r_lines[i] if i < len(r_lines) else " " * rw
                row = " " * shift + left_part + " " * gap + right_part
                lines.append(row.ljust(width))
            return lines, shift + mid

        for line in build(root)[0]:
            print(line.rstrip())

sol = Solution()
root = sol.build_tree([1,2,3,None,None,4])
root2 = sol.build_tree([1,2,3,4,None,None,5,6,None,None,7])
root3 = sol.build_tree([5, 3, 8, 1, None, 7, 9, None, 2, 6])
print()
sol.print_tree(root)
print(sol.is_balanced(root))
print()
print("="*50)
print()
sol.print_tree(root2)
print(sol.is_balanced(root2))
print()
print("="*50)
print()
sol.print_tree(root3)
print(sol.is_balanced(root3))