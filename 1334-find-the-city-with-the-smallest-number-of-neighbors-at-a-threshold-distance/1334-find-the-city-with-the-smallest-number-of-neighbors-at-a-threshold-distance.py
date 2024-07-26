class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        reachable_cities = {i:0 for i in range(n)}
        def bfs(start_node):
            visited = [False] * n
            heap = [(0, start_node)]

            while heap:
                curr_dist, node = heappop(heap)
                if visited[node]:
                    continue

                visited[node] = True
                reachable_cities[start_node] += 1
                
                for nei, weight in graph[node]:
                    if curr_dist + weight <= distanceThreshold and not visited[nei]:
                        heappush(heap, (curr_dist + weight, nei))
        
        for i in range(n):
            bfs(i)

        reachable_cities = list(sorted(reachable_cities.items(), key = lambda x: (x[1], -x[0])))
        return reachable_cities[0][0]
        

            
            

