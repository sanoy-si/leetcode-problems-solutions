class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        answer = 0
        stack = []
       
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
               ind = stack.pop()

               left = (ind - stack[-1] - 1) if stack else ind
               right = i - ind - 1 

               answer += (left + 1) * (right + 1) * arr[ind]
            
            stack.append(i)
        
        while stack:
            ind = stack.pop()

            left = (ind - stack[-1] - 1) if stack else ind
            right = len(arr) - ind - 1 

            answer += (left + 1) * (right + 1) * arr[ind]
        
        return int(answer % (1e9 + 7))