"""
Time complexity : O(N)
Space Complexity: O(N)

"""
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