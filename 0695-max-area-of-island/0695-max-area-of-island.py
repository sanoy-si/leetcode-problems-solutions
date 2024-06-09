class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def in_bound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        dirns = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def dfs(i, j):
            stack = [(i, j)]
            answer = 0
            while stack:
                i, j = stack.pop()
                if (i, j) in visited:
                    continue
                
                visited.add((i, j))
                answer += 1

                for d_i, d_j in dirns:
                    new_i, new_j = i + d_i, j + d_j
                    if in_bound(new_i, new_j) and (new_i, new_j) not in visited and grid[new_i][new_j]:
                        stack.append((new_i, new_j))
            
            return answer
            
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j]:
                    answer = max(answer, dfs(i, j))
        
        return answer