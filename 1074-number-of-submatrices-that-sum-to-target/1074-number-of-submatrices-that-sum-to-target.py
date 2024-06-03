class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        prefix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + matrix[i - 1][j - 1]

        answer = 0
        for r1 in range(n + 1):
            for r2 in range(r1 + 1, n + 1):
                prefixes = Counter()
                for c in range(m + 1):
                    current_sum = prefix[r2][c] - prefix[r1][c]
                    answer += prefixes[current_sum - target]
                    prefixes[current_sum] += 1
        
        return answer
                    
