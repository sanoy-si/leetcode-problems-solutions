class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        max_width = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    if j == 0:
                        max_width[i][j] = 1 
                    else:
                        max_width[i][j] = max_width[i][j - 1] + 1
        
        answer = 0
        for j in range(m):
            for bottom in range(n):
                curr_width = inf
                for top in range(bottom, -1, -1):
                    curr_width = min(curr_width, max_width[top][j])
                    answer = max(answer, curr_width * (bottom - top + 1))
                
        return answer
  