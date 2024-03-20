# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def findTarget(node , target , path):
            if node.val == target:
                return True
            if node.left and findTarget(node.left , target , path):
                path += 'L'
            elif  node.right and findTarget(node.right , target , path):
                path += 'R'
            return path

        start = []
        dest = []
        findTarget(root , startValue , start)
        findTarget(root , destValue ,dest)

        while start and dest and start[-1] == dest[-1]:
            start.pop()
            dest.pop()

        return "".join("U" * len(start)) + "".join(reversed(dest))
        