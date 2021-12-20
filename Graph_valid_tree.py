"""
Time Complexity = O(V+E)
Space Complexity = O(V+E)
"""

# Approach 1 DFS:

from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n:
            return False
        
        if n == 1:
            return True
        
        
        adj_list = defaultdict(list)
        
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)            
        
        visited = set()
        
        def dfs(node, parent):            
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited:
                    return False                
                
                result = dfs(neighbour, node)
                if not result:
                    return False
            return True            
            
        return dfs(0, -1) and len(visited) == n



# BFS
from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n:
            return False
        
        if n == 1:
            return True
        
        
        adj_list = defaultdict(list)
        
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)            
        
        visited = {0: -1}
        queue = deque([0])
        
        while queue:
            node = queue.popleft()
            for neighbour in adj_list[node]:                
                if neighbour == visited[node]:
                    continue
                if neighbour in visited:
                    return False                
                visited[neighbour] = node
                queue.append(neighbour)
                
        return len(visited) == n