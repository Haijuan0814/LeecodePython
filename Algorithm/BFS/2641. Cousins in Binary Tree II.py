# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        root.val = 0
        queue = deque([root])
        while queue:
            sum_level = 0
            cur = queue
            queue = []
            # caculate the sum of this level
            for node in cur:
                if node.left: 
                    sum_level += node.left.val
                if node.right: 
                    sum_level += node.right.val

            # sum - current sum = counsins' sum
            for node in cur:
                sum_cousins = sum_level
                if  node.left: sum_cousins -= node.left.val
                if  node.right: sum_cousins -= node.right.val

                if node.left: 
                    node.left.val = sum_cousins
                    queue.append(node.left)
                if node.right: 
                    node.right.val = sum_cousins
                    queue.append(node.right)
        return root

        

""" deque（double-ended queue）是一个双端队列数据结构，它允许在队列的两端进行高效地插入和删除操作
支持以下主要操作：
append(x): 在deque的右侧添加元素x。
appendleft(x): 在deque的左侧添加元素x。
pop(): 移除并返回deque的最右侧的元素。
popleft(): 移除并返回deque的最左侧的元素。
extend(iterable): 在deque的右侧扩展添加一个可迭代对象中的所有元素。
extendleft(iterable): 在deque的左侧扩展添加一个可迭代对象中的所有元素，注意添加顺序与可迭代对象相反。
rotate(n): 将deque向右旋转n步（如果n是负数，则向左旋转）。 """
        