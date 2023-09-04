class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.l = [-1 for i in graph]
        def dfs(i,parent = None):
            if self.l[i] == parent:return False
            if self.l[i] != -1:return True
            self.l[i] = 0 if parent else 1

            for j in graph[i]:
                if not dfs(j,self.l[i]):return False
            return True 
        for i in range(len(graph)):
            if not dfs(i):return False
        return True
        