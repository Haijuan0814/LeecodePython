# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        minHeap = []
        ListNode.__lt__ = lambda self , other : self.val < other.val


        # push listNode into minHeap. minHeap Order by first number of these listNodes
        for l in lists:
            if l:
                heapq.heappush(minHeap,l)
        
        dummyNode = ListNode(0)
        currNode = dummyNode
        while minHeap:
            # node = the listnode with smallest first number
            node = heapq.heappop(minHeap)
            currNode.next = node
            currNode = currNode.next
            node = node.next
            if node:
                heapq.heappush(minHeap,node)
        
        return dummyNode.next

     

""" 

知识点总结：
1、向heap中 insert ListNode

2、魔术方法
 __init__: 初始化方法，用于初始化对象的状态。
__repr__: 返回对象的“官方”字符串表示，通常用于调试和日志记录。
__str__: 返回对象的“非官方”字符串表示，通常用于用户友好的输出。
__eq__: 定义对象相等性比较的方法，用于 == 运算符。
__ne__: 定义对象不等性比较的方法，用于 != 运算符。
__lt__, __le__, __gt__, __ge__: 分别定义对象的小于、小于等于、大于、大于等于比较的方法，用于 <, <=, >, >= 运算符。
__len__: 定义对象的长度，用于内置函数 len()。
__getitem__, __setitem__, __delitem__: 定义对象的索引访问、赋值和删除方法，用于下标操作。
__iter__, __next__: 定义对象的迭代器方法，使对象可以被迭代。
__contains__: 定义对象的成员包含测试方法，用于 in 运算符。
__call__: 使对象可以像函数一样被调用。 """