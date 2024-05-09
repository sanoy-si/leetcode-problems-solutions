class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memory = {}

        def dp(idx):
            if idx >= n:
                return 0
            
            if idx not in memory:
                memory[idx] = max(dp(idx + 1), nums[idx] + dp(idx + 2))

            return memory[idx]
            
        
        return dp(0)