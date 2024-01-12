class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(lambda: [[]])
        for a,b in prerequisites:
            graph[b][0].append(a)
            graph[b].append(0)
        
        def dfs(i):
            if i not in graph:
                return True
            if graph[i][1] == 1:
                return False
            if graph[i][1] == 2:
                return True
            
            graph[i][1] = 1

            for neighbour in graph[i][0]:
                if dfs(neighbour) == False:
                    return False
            
            graph[i][1] = 2

            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True
        
