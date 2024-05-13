class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memory = {}

        def dp(idx):
            if idx >= len(nums):
                return 0
            
            if idx not in memory:
                memory[idx] = 1

                for i in range(idx + 1, len(nums)):
                    if nums[idx] < nums[i]:
                        memory[idx] = max(memory[idx], 1 + dp(i))

            return memory[idx]
        

        ans = 1
        for i in range(len(nums)):
            ans = max(ans, dp(i))

        return ans
            