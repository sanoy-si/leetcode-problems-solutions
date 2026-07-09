class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]    
            x = self.parent[x]

        return x
    
    def union(self, x, y):
        x_parent, y_parent = self.parent[x], self.parent[y]
        if x_parent != y_parent:
            if self.size[x_parent] > self.size[y_parent]:
                self.parent[y_parent] = x_parent
                self.size[x_parent] += self.size[y_parent]
            
            else:
                self.parent[x_parent] = y_parent
                self.size[y_parent] += self.size[x_parent]
            


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        for i in range(n - 1):
            if abs(nums[i] - nums[i + 1]) <= maxDiff:
                dsu.union(i, i + 1)
        
        answer = []
        for u, v in queries:
            answer.append(dsu.find(u) == dsu.find(v))
        
        return answer
                
