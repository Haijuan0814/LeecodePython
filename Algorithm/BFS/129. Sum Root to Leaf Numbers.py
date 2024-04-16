# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        

        total = 0
        def dfs(root , num):
            nonlocal total
            if root is None:
                return 0
            
            num = num * 10 + root.val
            if root.left is None and root.right is None:
                total += num
            if root.left:
                dfs(root.left , int(num))
            if root.right:
                dfs(root.right , int(num))
        dfs(root , 0)
        return total