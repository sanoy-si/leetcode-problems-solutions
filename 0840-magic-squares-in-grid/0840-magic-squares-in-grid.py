class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        answer = 0
        n = len(grid)
        for i in range(n - 3 + 1):
            for j in range(n - 3 + 1):
                if sum(grid[i][j:j + 3]) == sum(grid[i + 1][j:j+3]) == sum(grid[i + 2][j:j+3]) and grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] == grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]:
                    answer += 1
        
        return answer