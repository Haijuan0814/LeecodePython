# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        slow = fast = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse slow
        slow.next, slow= None, slow.next
        prev = None
        while slow:
            current = slow
            slow = slow.next
            current.next = prev
            prev = current
        
        # get the new head
        first, second = head, prev
        while second:
            first.next, first = second, first.next
            second.next, second = first, second.next
           