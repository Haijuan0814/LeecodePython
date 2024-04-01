class SegmentTree:
    def __init__(self , n):
        self.tree = [0] * n
    
    # 计算指定范围内
    def query(self , left , right , n):
        total = 0
        left += n
        right += n
        while left < right:
            if left & 1:
                total += self.tree[left]
                left += 1
            left = left // 2

            if right & 1:
                right -= 1
                total += self.tree[right]
            right = right // 2 
        return total
    
    # 在指定位置更新值n
    def update(self,index,value,n):
        index += n
        self.tree[index] += value
        while index > 1:
            index = index//2
            self.tree[index] = self.tree[2*index] + self.tree[2*index+1]


class Solution:
    def createSortedArray(self, instructions):
        _max, cost = max(instructions)+1, 0
        result = SegmentTree(2 * _max)

        for x in instructions:
            left_cost = result.query(0 , x , _max)
            right_cost = result.query(x + 1 , _max , _max)
            cost += min(left_cost , right_cost)
            result.update( x , 1 , _max)

        return cost%(10**9+7)
        








""" 
运行是错误的， 但没理解为什么错， 尴尬
# BST Solution
# 1. Create a Tree, left < node < right
# 2. Find numbers of lessthan and greaterthan

class TreeNode:
    def __init__(self , val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1 # number of same values in this node

class Solution:
    # insert a value to a Tree
    def insert(self, root , val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left , val)
        elif val > root.val:
            root.right = self.insert(root.right , val)
        else:
            root.count += 1

        return root

    # count numbers : less than val and greater than val
    def count_less_and_greater(self, root , val):
        less , greater = 0 , 0
        if not root:
            return less , greater
        
        while root:
            if val < root.val:
                greater += 1 
                root = root.left
            elif val > root.val:
                less += 1 
                root = root.right
            else:
                # greater += root.count 
                # less += root.count  
                break
        return less , greater

    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10**9 + 7
        cost = 0
        root = None

        for num in instructions:
            less , greater = self.count_less_and_greater(root , num)
            cost += min(less , greater)
            root = self.insert(root , num)

        return cost % mod
    
         """