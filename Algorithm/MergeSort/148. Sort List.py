# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # divide to find the mid
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next

        # get the left and right
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)

        res = ListNode(0)
        temp = res
        while left and right:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        if left:
            temp.next = left
        if right:
            temp.next = right
        return res.next



# solution2 , MergeSort, Not Efficient       
class Solution1:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # divide 
        def mergesort(listnode):
            if not listnode.next:
                return listnode
            curr = ListNode(listnode.val)
            _next = mergesort(listnode.next)
            return merge(curr , _next)
        # sort and merge
        def merge(node1 , node2):
            res = ListNode(0)
            temp = res
            while node1 and node2:
                if node1.val <= node2.val:
                    temp.next = node1
                    node1 = node1.next
                else:
                    temp.next = node2
                    node2 = node2.next
                temp = temp.next
            if node1:
                temp.next = node1
            if node2:
                temp.next = node2
            return res.next

        return mergesort(head)