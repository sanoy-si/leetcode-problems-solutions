class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

    
        items = list(graph.items())
        print(items)
        v = 0
        for item in items:
            if len(item[1]) == len(items) - 1:
                return item[0]
        

            
        