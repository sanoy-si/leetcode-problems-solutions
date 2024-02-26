class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        cols = [float('-inf') for i in range(len(grid[0]))]
        rows = [max(row) for row in grid]

        for col in range(len(grid[0])):
            for row in range(len(grid)):
                cols[col] = max(cols[col], grid[row][col])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                ans += max(0, min(cols[col], rows[row]) - grid[row][col])

        return ans  
        
        