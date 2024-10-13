class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        graph =[[] for _ in range(n)]
        for u, v in prerequisites:
            graph[u].append(v)

        def add_predecessors(node):
            visited = [False] * n
            in_time, out_time = [-1] * n, [-1] * n
            timer = 0

            def dfs(node):
                nonlocal timer
                in_time[node] = timer
                timer += 1
                for child in graph[node]:
                    if not visited[child]:
                        dfs(child)
                
                out_time[node] = timer
                timer += 1
            
            dfs(node)
            for i in range(n):
                if in_time[i] != -1 and in_time[node] < in_time[i] < out_time[i] < out_time[node]:
                    ancestors.add((node, i))
        
        ancestors = set()
        for node in range(n):
            add_predecessors(node)
        
        answer = []
        for ancestor, predecessor in queries:
            answer.append((ancestor, predecessor) in ancestors)

        return answer

            




        
        

        