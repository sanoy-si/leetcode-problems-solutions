class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        min_range = {}
        n = len(heights)
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                left = idx - stack[-1] - 1 if stack else i
                right = i - idx - 1
                min_range[idx] = left + right + 1
            stack.append(i)
        
        while stack:
            idx = stack.pop()
            left = idx - stack[-1] - 1 if stack else i
            right = n - idx - 2
            min_range[idx] = left + right + 1
        
        answer = 0
        for i in range(n):
            answer = max(answer, heights[i] * min_range[i])

        return answer
