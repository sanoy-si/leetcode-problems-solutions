class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        answer = 0
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                curr_idx = stack.pop()
                left_bound = curr_idx - stack[-1] - 1 if stack else curr_idx
                right_bound = i - curr_idx - 1
                answer += ((left_bound + 1)* (right_bound + 1)) * arr[curr_idx]
            
            stack.append(i)
        
        while stack:
            curr_idx = stack.pop()
            left_bound = curr_idx - stack[-1]- 1 if stack else curr_idx
            right_bound = len(arr) - curr_idx - 1
            answer += ((left_bound + 1)* (right_bound + 1)) * arr[curr_idx]
        
        return answer