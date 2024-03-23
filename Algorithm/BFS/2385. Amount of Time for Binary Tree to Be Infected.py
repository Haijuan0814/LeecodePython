from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # initial graph into list
    graph = []
    def init_graph(self,  node):
        if node.left:
            self.graph[node.val].append(node.left.val)
            self.graph[node.left.val].append(node.val)
            self.init_graph(node.left)
        if node.right:
            self.graph[node.val].append(node.right.val)
            self.graph[node.right.val].append(node.val)
            self.init_graph(node.right)

    def height(self, node, pre):
        if node == None:
            return -1
        else:
            m = -1
        for x in self.graph[node]:
            if x != pre:
                m = max(m, self.height(x, node))
        return 1 + m


    def amountOfTime(self, root: TreeNode, start: int) -> int:
        if not root:
            return 0

        self.graph = defaultdict(list)
        self.init_graph(root)
        return self.height(start, -1)

   
        
"""         # Construct adjacency list graph
        graph = {}
        queue = deque([(root, None)])  # Use None as parent of root
        while queue:
            node, parent = queue.popleft()
            if node.val not in graph:
                graph[node.val] = set()
            if parent:
                graph[node.val].add(parent.val)
                graph[parent.val].add(node.val)
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
        
        # Perform BFS to infect nodes
        infected = set([start])
        minutes = 0
        while infected:
            new_infected = set()
            for node in infected:
                for neighbor in graph[node]:
                    if neighbor not in infected:
                        new_infected.add(neighbor)
            infected = new_infected
            minutes += 1
        
        return minutes - 1  # Subtract 1 since the first minute is minute 0 """
