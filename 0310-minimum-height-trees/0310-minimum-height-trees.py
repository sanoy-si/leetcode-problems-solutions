class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if not edges:
            return [0]
            
        graph = [[] for _ in range(n)]
 
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        queue = deque()
        indegrees = [0 for _ in range(n)]

        for i in range(n):
            if len(graph[i]) == 1:
                queue.append(i)
            
            indegrees[i] += len(graph[i])

        while queue:
            if n <= 2:
                return queue

            for _ in range(len(queue)):
                node = queue.popleft()

                n -= 1

                for neighbour in graph[node]:
                    indegrees[neighbour] -= 1
                    
                    if indegrees[neighbour] == 1:
                        queue.append(neighbour)


                