class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.path = []
        def dfs(arr,node):
            if arr and arr[-1] == len(graph) - 1:
                self.path.append(arr[:])
            for i in graph[node]:
                arr.append(i)
                dfs(arr,i)
                arr.pop()
        dfs([0],0)
        return self.path
        