# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        graph = deque([root])
        res = []
        while graph:
            max_val = float('-inf')
            for _ in range(len(graph)):
                node = graph.popleft()
                max_val = max(max_val, node.val)
                if node.left: graph.append(node.left)
                if node.right: graph.append(node.right)
            res.append(max_val)
        return res