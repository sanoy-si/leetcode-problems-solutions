class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1

        prerequisites = [set() for _ in range(numCourses)]
        

        def bfs():
            queue = deque([i for i in range(numCourses) if indegree[i] == 0])

            while queue:
                node = queue.popleft()

                for neighbour in graph[node]:
                    indegree[neighbour] -= 1
                    prerequisites[neighbour] |= prerequisites[node]
                    prerequisites[neighbour].add(node)

                    if indegree[neighbour] == 0:
                        queue.append(neighbour) 
                
        bfs()

        answer = []

        for a, b in queries:
            answer.append(a in prerequisites[b])
        
        return answer
