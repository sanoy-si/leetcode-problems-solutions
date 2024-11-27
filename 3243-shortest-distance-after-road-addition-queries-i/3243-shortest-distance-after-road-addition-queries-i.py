class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for i in range(1, n):
            graph[i - 1].append(i)

        def find_shortest_length(graph):
            queue = deque([0])
            count = 0
            added = set([0])
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node == n - 1:
                        return count

                    for child in graph[node]:
                        if child not in added:
                            queue.append(child)
                            added.add(child)
                count += 1
        
        answer = []
        for u, v in queries:
            graph[u].append(v)
            answer.append(find_shortest_length(graph))
        
        return answer


