# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        newroot = root
        def dfs( root , curr ):
            if not root:
                return

            if curr+1 == depth:
                #if root.left:
                val1 = TreeNode(val)
                tmp = root.left
                root.left = val1
                val1.left = tmp

                #if root.right:
                val2 = TreeNode(val)
                tmp = root.right
                root.right =  val2
                val2.right = tmp

                return
            else:
                curr += 1
                dfs(root.left , curr)
                dfs(root.right , curr)
        if depth == 1:
            val1 = TreeNode(val)
            val1.left = root
            root = val1
        else:
            dfs(newroot , 1)
        return root



        