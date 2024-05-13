class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        for i in range(n):
            if grid[i][0] == 0:
                grid[i] = [0 if grid[i][j] else 1 for j in range(m)]


        transpose = list(zip(*grid))
        answer = 0
        for i in range(len(transpose)):
            one_count = transpose[i].count(1)

            answer += max(one_count, n - one_count) * (2 ** (m - i - 1))
        
        return answer