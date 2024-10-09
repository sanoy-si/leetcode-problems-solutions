class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def top_sort(node):
            color[node] = 1 
            for child in graph[node]:
                if color[child] == 0:
                    top_sort(child)
            
            color[node] = 2
            order.append(node)
            
        order = []
        color = [0] * numCourses
    
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        for node in range(numCourses):
            if color[node] == 0:
                top_sort(node)

        return order[::-1] if len(order) == numCourses else []
        