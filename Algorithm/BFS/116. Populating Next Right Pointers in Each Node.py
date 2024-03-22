"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root :
            return root
        
        root.next = None

        graph = deque([root])
        while graph:
            prev = None
            for _ in range(len(graph)):
                node = graph.popleft()
                node.next = prev
                prev = node
                if node.left:
                    graph.append(node.right)
                    graph.append(node.left)
        return root