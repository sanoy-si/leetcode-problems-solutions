class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        graph =[[] for _ in range(n)]
        for u, v in prerequisites:
            graph[u].append(v)

        def add_predecessors(node):
            time_in, time_out = [-1] * n, [-1] * n
            def dfs(start):
                timer = 0 
                color = [0] * n
                stack = [start]
                while stack:
                    node = stack[-1]
                    if color[node] == 0:
                        time_in[node] = timer
                        timer += 1
                        color[node] = 1

                        for child in graph[node]:
                            if color[child] == 0:
                                stack.append(child)  

                    else:
                        stack.pop()
                        time_out[node] = timer
                        timer += 1
            
            dfs(node)
            for i in range(n):
                if time_in[i] != -1 and time_in[node] < time_in[i] < time_out[i] < time_out[node]:
                    is_ancestor[node][i] = True
        
        is_ancestor = [[False for _ in range(n)] for _ in range(n)] 
        for node in range(n):
            add_predecessors(node)
        
        answer = []
        for ancestor, predecessor in queries:
            answer.append(is_ancestor[ancestor][predecessor])

        return answer

            




        
        

        