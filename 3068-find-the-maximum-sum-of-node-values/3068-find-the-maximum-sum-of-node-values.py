class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:

        memo = {}
        def dp(idx, changed):
            if idx == len(edges):
                return sum(nums)
            
            if idx not in memo:
                dont_change = dp(idx + 1, False)

                nums[edges[idx][0]] ^= k
                nums[edges[idx][1]] ^= k
                change = dp(idx + 1, True)

                memo[idx, changed] = max(change, dont_change)
            
            return memo[idx, changed]
        
        ans = dp(0, False)

        return ans
