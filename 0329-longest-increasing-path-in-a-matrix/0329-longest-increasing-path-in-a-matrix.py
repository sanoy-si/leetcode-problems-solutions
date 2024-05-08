class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        paths = [[0 for _ in range(m)] for _ in range(n)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inbound = lambda i, j: 0 <= i < n and 0 <= j < m

        def dfs(i, j):
            if paths[i][j] != 0:
                return paths[i][j]
            
            curr = 1

            for di, dj in dirs:
                newi, newj = i + di, j + dj

                if inbound(newi, newj) and matrix[newi][newj] > matrix[i][j]:
                    curr = max(dfs(newi, newj) + 1, curr)
            
            paths[i][j] = curr

            return curr
        
        answer = 0
        for i in range(n):
            for j in range(m):
                answer = max(dfs(i, j), answer)
        
        return answer 
                