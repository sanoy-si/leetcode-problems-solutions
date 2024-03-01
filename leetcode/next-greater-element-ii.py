class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []

        answer = [-1 for i in range(len(nums))]

        for i in range(len(nums) * 2):
            while stack and nums[stack[-1]] < nums[i % len(nums)]:
                answer[stack.pop()] = nums[i % len(nums)]

            stack.append(i % len(nums))
        
        return answer