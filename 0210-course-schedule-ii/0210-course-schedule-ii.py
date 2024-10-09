class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def top_sort(node):
            if color[node] == 1:
                return False

            color[node] = 1 
            for child in graph[node]:
                if color[child] != 2:
                    if not top_sort(child):
                        return False
            
            color[node] = 2
            order.append(node)
            return True


        order = []
        color = [0] * numCourses
        
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        for node in range(numCourses):
            if color[node] == 0:
                if not top_sort(node):
                    return []

        return order[::-1] 
        