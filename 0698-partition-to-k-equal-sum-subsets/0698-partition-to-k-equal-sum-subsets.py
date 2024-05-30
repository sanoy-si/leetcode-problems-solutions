class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) / k
        if target != int(target):
            return False

        n = len(nums)
        memo = [[[-1 for _ in range(k + 1)] for _ in range((1 << n))] for _ in range(n)]
        def dp(idx, curr_sum, mask, k):
            if k == 0:
                return True

            if idx == n:
                if curr_sum == target:
                    return dp(0, 0, mask, k - 1)
                
                return False
            if memo[idx][mask][k] == -1: 
                curr_result = False
                if mask & 1 << idx == 0 and dp(idx + 1, curr_sum + nums[idx], mask | 1 << idx, k):
                    curr_result = True
                
                if dp(idx + 1, curr_sum, mask, k):
                    curr_result = True
                
                memo[idx][mask][k] = curr_result

            return memo[idx][mask][k]
        
        return dp(0, 0, 0, k)