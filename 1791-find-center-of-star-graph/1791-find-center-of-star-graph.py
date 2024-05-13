class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(len(edges) + 2)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(1, len(edges) + 2):
            if len(graph[i]) == len(edges):
                return i
                
        print(graph)
        return 1
