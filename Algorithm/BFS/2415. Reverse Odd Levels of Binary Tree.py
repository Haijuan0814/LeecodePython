# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left:
            return root

        queue = deque()
        queue.append((root.left , root.right , 1))
        while queue:
            l , r , level = queue.popleft()
            if level % 2 ==1:
                l.val , r.val = r.val , l.val
            if l.left:
                queue.append((l.left, r.right, level+1))
                queue.append((l.right, r.left, level+1))

        return root


   


                    
        