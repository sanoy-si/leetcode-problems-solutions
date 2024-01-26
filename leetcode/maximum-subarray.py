class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            curr_sum = max(curr_sum, 0)
        
        return max_sum