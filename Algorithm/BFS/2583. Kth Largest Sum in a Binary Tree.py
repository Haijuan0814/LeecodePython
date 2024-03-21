# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        #if k == 0:
            #return root.val

        queue = deque([root]) 
        # level = 0
        sum_list = [root.val]
        #sum_list.add(root.val)
        while queue:
            # level += 1
            sum_level = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    sum_level += node.left.val
                    queue.append(node.left)
                if node.right:
                    sum_level += node.right.val
                    queue.append(node.right)
            sum_list.append(sum_level)
        
        if k >= len(sum_list):
            return -1
        sum_list = sorted(sum_list , reverse = True)
        return sum_list[k-1]
            