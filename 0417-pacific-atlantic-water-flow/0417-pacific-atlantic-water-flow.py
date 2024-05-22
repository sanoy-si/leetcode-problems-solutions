class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        can = [[[-1, -1] for _ in range(m)] for _ in range(n)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        inbound = lambda i, j: 0 <= i < n and 0 <= j < m

        def dfs(i, j, check):
            ans = False

            if check == 'Pacific':
                if j < 0 or i < 0:
                    return True

                if not inbound(i, j):
                    return False

                if can[i][j][0] == -1:
                    
                    visited[i][j] = True

                    for di, dj in dirs:
                        newi, newj = i + di, j + dj
                        if not inbound(newi, newj) or (not visited[newi][newj] and heights[i][j] >= heights[newi][newj]): 
                            new_ans = dfs(newi, newj, 'Pacific')
                            ans = ans or new_ans
                    
                    visited[i][j] = False

                    can[i][j][0] = ans
                
                return can[i][j][0]
            
            else:
                if i >= n or j >= m:
                    return True
                
                if not inbound(i, j):
                    return False
                
                if can[i][j][1] == -1:
                    visited[i][j] = True

                    for di, dj in dirs:
                        newi, newj = i + di, j + dj
                        if not inbound(newi, newj) or (not visited[newi][newj]) and heights[i][j] >= heights[newi][newj]:
                            new_ans = dfs(newi, newj, 'Atlantic')
                            ans = ans or new_ans
                        
                        visited[i][j] = False

                        can[i][j][1] = ans
                    
                return can[i][j][1]
        
        for i in range(n):
            for j in range(m):
                dfs(i, j, "Pacific")
                dfs(i, j, "Atlantic")
        
        answer = [[i, j] for j in range(m) for i in range(n) if can[i][j][0] == True and can[i][j][1] == True]

        return answer
                


