# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # abb - 011
        # aba - 010
        # bbb - 111
        # ab - 01

        def dfs(root , path):
            if not root:
                return
            path = chr(root.val + ord('a')) + path

            if not root.left and not root.right: 
                return path

            left_path = dfs(root.left, path)
            right_path = dfs(root.right, path)
            if left_path and right_path: 
                return min(left_path, right_path)
            elif left_path:  
                return left_path
            else:  
                return right_path
        return dfs(root, "")