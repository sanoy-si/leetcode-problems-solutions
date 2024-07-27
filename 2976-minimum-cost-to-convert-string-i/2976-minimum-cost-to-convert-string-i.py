class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def find_shortest_path(start, end):
            visited = defaultdict(bool)
            heap = [(0, start)]

            while heap:
                curr_cost, node = heappop(heap)
                if node == end:
                    return curr_cost
                
                if visited[node]:
                    continue
                visited[node] = True

                for cost, nei in graph[node]:
                    if not visited[nei]:
                        heappush(heap, (curr_cost + cost, nei))
                
            return -1
        

        graph = defaultdict(list)
        for i in range(len(original)):
            graph[original[i]].append((cost[i], changed[i]))
        

        answer = 0
        distances = {}
        for i in range(len(source)):
            start, end = source[i], target[i]
            if (start, end) not in distances:
                distances[(start, end)] = find_shortest_path(start, end)
                if distances[(start, end)] == -1:
                    return -1
            
            answer += distances[(start, end)]
        
        return answer

                