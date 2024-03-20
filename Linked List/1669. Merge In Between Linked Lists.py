# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        # get nodes from 0 to a-1
        tmp1 = list1
        for _ in range(a-1):
            tmp1 = tmp1.next
        
        # filter the nodes from a to b
        # get the last nodes and save in tmp2
        tmp2 = tmp1
        for _ in range(b - a + 2):
            tmp2 = tmp2.next

        # get the nodes from list2
        tmp1.next = list2
        while list2.next:
            list2 = list2.next

        list2.next = tmp2
        return list1

        

        # solution2 , not efficient

        """ res = ListNode(0)
        tmp = res
        i = 0
        while list1:
            if i < a or i > b:
                tmp.next = list1
                tmp = tmp.next
                list1 = list1.next
                if i == a-1:
                    while list2:
                        tmp.next = list2
                        tmp = tmp.next
                        list2 = list2.next
            elif a <= i <= b:
                # 过滤list1
                list1 = list1.next
            i += 1
        return res.next """