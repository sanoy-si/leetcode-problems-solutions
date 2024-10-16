class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        down_count = m - 1
        right_count = n - 1

        return factorial(down_count + right_count) // (factorial(down_count) * factorial(right_count))