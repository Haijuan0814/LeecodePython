""" You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807. """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        resultNode = ListNode()
        tmpNode = resultNode
        while (l1 or l2 or carry):
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            total = num1 + num2 + carry

            num = total % 10
            carry = total // 10

            tmpNode.next = ListNode(num)
            tmpNode = tmpNode.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return resultNode.next


    # Solution -2
    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = self.getDecimal(l1)
        sum2 =  self.getDecimal(l2)
        totalSum = sum1+sum2
        
        result = ListNode()
        current = result
        for digit in str(totalSum)[::-1]:
            current.next = ListNode(int(digit))
            current = current.next
        return result.next
        
    def getDecimal(self,list):
        sum = 0 
        while(list):
            sum = sum*10 + list.val
            list = list.next
        return sum
        

    
    

        