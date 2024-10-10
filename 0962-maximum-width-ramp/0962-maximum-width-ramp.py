class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        answer = 0
        for i in range(len(nums)):

            idx = bisect_left(stack, -nums[i], key = lambda x: -nums[x])
            if idx < len(stack):
                answer = max(answer, i - stack[idx])

            if stack and nums[stack[-1]] <= nums[i]:
                continue
            
            stack.append(i)
        
        return answer
