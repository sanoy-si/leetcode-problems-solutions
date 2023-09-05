

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        s = set()

        def dfs(node):
            if node == destination:return True
            if node in s:return False
            
            s.add(node)
            for i in graph[node]:
                if dfs(i):return True
            return False
        return dfs(source)
             
        
            
        
        