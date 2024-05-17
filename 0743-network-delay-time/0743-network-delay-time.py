class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for a, b, w in times:
            graph[a].append((b, w))
        
        start = k
        distance = {i:inf for i in range(1, n + 1)}
        queue = [(start, 0)]

        while queue:
            node, dist = heappop(queue)
            
            if distance[node] != inf:
                continue

            distance[node] = dist

            for nei, nei_dist in graph[node]:
                if distance[nei] == inf:
                    heappush(queue, (nei, nei_dist + dist))
        
        answer = max(distance.values())

        return answer if answer != inf else -1
        