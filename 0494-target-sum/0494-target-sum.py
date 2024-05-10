class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memory = {}

        def dp(idx, curr_sum):
            if idx >= n:
                return curr_sum == target
            
            if (idx, curr_sum) not in memory:
                memory[(idx, curr_sum)] = dp(idx + 1, curr_sum + nums[idx]) + dp(idx + 1, curr_sum - nums[idx])
            
            return memory[(idx, curr_sum)]
        
        return dp(0, 0)

                