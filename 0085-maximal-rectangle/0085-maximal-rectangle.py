class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def find_max_area(heights):
            stack = []
            min_range = {}
            n = len(heights)
            for i in range(n):
                while stack and heights[stack[-1]] > heights[i]:
                    idx = stack.pop()
                    left = idx - stack[-1] - 1 if stack else idx
                    right = i - idx - 1
                    min_range[idx] = left + right + 1
                stack.append(i)
            
            while stack:
                idx = stack.pop()
                left = idx - stack[-1] - 1 if stack else idx
                right = n - idx - 1
                min_range[idx] = left + right + 1
            
            answer = 0
            for i in range(n):
                answer = max(answer, heights[i] * min_range[i])

            return answer
        
        n = len(matrix)
        m = len(matrix[0])
        heights = [0 for _ in range(m)]
        answer = 0

        for i in range(n):
            for j in range(m):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            answer = max(answer, find_max_area(heights))
        
      
        
        return answer
            