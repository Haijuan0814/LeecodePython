# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node.val == 0:
                return False
            elif node.val == 1:
                return True
            elif node.val == 2:
                return (dfs(node.left) if node.left else False) or (dfs(node.right) if node.right else False)
            elif node.val == 3:
                return (dfs(node.left) if node.left else True) and (dfs(node.right) if node.right else True)
        
        return dfs(root)
        