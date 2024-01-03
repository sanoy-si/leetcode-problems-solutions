class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        answer = float('-inf')
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if i + 2 >= row or j + 2 >= col:
                    continue
                current = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                answer = max(answer, current)

        return answer

        