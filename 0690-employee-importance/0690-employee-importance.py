"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.importance = 0
        self.graph = defaultdict(list)
        self.visited = set()
        for i in employees:
            self.graph[i.id] = [i.importance,i.subordinates]
        
        
        def dfs(i):
            if i in self.visited:return
            self.visited.add(i)
            self.importance += self.graph[i][0]
            
            for j in self.graph[i][1]:
                dfs(j)
        dfs(id)
        return self.importance
        
        