# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = self.reverse_list(head)
        carry = 0
        current = reversed_list
        previous = None
        while current:
            val = current.val * 2 + carry
            current.val = val % 10
            carry = 1 if val > 9 else 0
            previous = current
            current = current.next

        if carry:
            previous.next = ListNode(carry)
        res = self.reverse_list(reversed_list)
        return res
     
    def reverse_list(self ,  node:ListNode) -> ListNode:
        previous , current = None , node
        while current:
            nextNode = current.next
            current.next = previous
            previous , current = current , nextNode
        return previous

