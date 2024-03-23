# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        return self.dfs(head , root)

    def checkNode(self ,  listNode ,  treeNode):
        if not listNode:
            return True
        elif not treeNode:
            return False

        elif listNode.val == treeNode.val:
            if self.checkNode(listNode.next , treeNode.left):
                return True
            else:
                return self.checkNode(listNode.next , treeNode.right)
        return False


    def dfs(self , head , root):
        if not root:
            return False

        if self.checkNode(head , root):
            return True

        if self.dfs(head , root.left):
            return True

        return self.dfs(head , root.right)
    
    
    



