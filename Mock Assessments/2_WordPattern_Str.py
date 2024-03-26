""" Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true """

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        arr = s.split()  
        n = len(pattern)
        if n != len(arr):
            return False
        
        pa_graph = defaultdict(list)
        str_graph = defaultdict(list)
        for i in range(n):
            pa_graph[pattern[i]].append(i)
            str_graph[arr[i]].append(i)
        
        if sorted(pa_graph.values()) == sorted(str_graph.values()):
            return True
        return False
            
       