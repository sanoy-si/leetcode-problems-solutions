class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[1]].add(edge[0])
        
        unreachables = set()
        for i in range(n):
            if len(graph[i]) == 0:
                unreachables.add(i)
        return unreachables
        