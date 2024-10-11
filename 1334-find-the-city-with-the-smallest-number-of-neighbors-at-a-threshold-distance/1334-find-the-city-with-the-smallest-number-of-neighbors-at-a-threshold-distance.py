class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[inf if i != j else 0 for i in range(n)] for j in range(n)]
        for u, v, w in edges:
            matrix[u][v] = matrix[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
        answer = [-1, -1]
        for node in range(n):
            for row in matrix[node]:
                count = len([i for i in range(n) if matrix[node][i] <= distanceThreshold])
                if answer[0] == -1 or answer[1] > count or answer[1] == count and node > answer[0]:
                    answer = [node, count]

        return answer[0]
