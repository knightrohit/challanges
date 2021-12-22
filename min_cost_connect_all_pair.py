"""
Time complexity : O(N)
Space Complexity: O(N)

"""

# Kruskal's algorithm
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
        class UnionFind:
            
            def __init__(self, n):
                self.root = list(range(n))
                self.rank = [1]*n
                
            def find(self, node):
                if node == self.root[node]:
                    return node
                
                self.root[node] = self.find(self.root[node])
                return self.root[node]
            
            def union(self, x, y):
                x_root = self.find(x)
                y_root = self.find(y)
                
                if x_root == y_root:
                    return False
                
                if self.rank[x_root] > self.rank[y_root]:
                    self.root[y_root] = x_root
                
                elif self.rank[y_root] > self.rank[x_root]:
                    self.root[x_root] = y_root
                    
                else:
                    self.root[y_root] = x_root
                    self.rank[x_root] += 1
                return True
        

        path_weight = []
        edges = 0
        out = 0
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                val = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                path_weight.append((val, i, j))                

        path_weight.sort()
        ds = UnionFind(n)
 
        for weight, p1, p2 in path_weight:
            if ds.union(p1, p2):
                out += weight
                edges += 1
                
        return out



"""
Time Complexity : O(E+V)*O(logV)
Space Complexity: O(V)
"""

# Prims Algorithm
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
            if not points:
                return 0            

            size = len(points)
            visited = set([0])
            x1, y1 = points[0]
            edges = []
            count = size - 1
            cost = 0
            
            for indx, val in enumerate(points[1:], start = 1):
                x2, y2 = val
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, 0, indx))
                
            heapq.heapify(edges)
            
            while edges and count > 0:
                dist, start, end = heapq.heappop(edges)
 
                if end not in visited:
                    visited.add(end)
                    cost += dist
                    for j in range(size):
                        if j not in visited:
                            x1, y1 = points[end]
                            x2, y2 = points[j]
                            diff = abs(x1-x2) + abs(y1-y2)
                            heapq.heappush(edges, (diff, end, j))
                    count -= 1                    
                    
            return cost