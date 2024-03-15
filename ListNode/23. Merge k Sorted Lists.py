# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        if length == 0:
            return None
        if length == 1:
            return lists[0]
        
        finalList = lists[0]
        for i in range(1,length):
            finalList = self.MergeTwoNode(finalList , lists[i])

        return finalList
        

    def MergeTwoNode(self, node1:Optional[ListNode] , node2:Optional[ListNode]):
        mergeNode = ListNode(0)
        curNode = mergeNode

        while node1 is not None and node2 is not None:
            if node1.val <= node2.val:
                curNode.next = node1
                curNode = curNode.next 
                node1 = node1.next
            else:
                curNode.next = node2
                curNode = curNode.next
                node2 = node2.next

        if node1 is not None : curNode.next = node1
        if node2 is not None : curNode.next = node2
        return mergeNode.next


        
        