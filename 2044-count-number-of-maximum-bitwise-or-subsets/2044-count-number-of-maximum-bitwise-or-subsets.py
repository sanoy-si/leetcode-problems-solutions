class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        answer = 0
        current = 0
        def backtrack(idx):
            nonlocal current, answer
            if idx == len(nums):
                if current == max_or:
                    answer += 1
                return
            
            original_current = current
            current |= nums[idx]
            backtrack(idx + 1)
            
            current = original_current
            backtrack(idx + 1)
            
        backtrack(0)

        return answer
