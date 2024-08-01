class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ind = 0
        p = 0
        
        while p <= max_ind < len(nums):
            max_ind = max(p + nums[p], max_ind)
            p += 1
        
        return max_ind >= len(nums) - 1

        