class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums ) / 2 
        
        def func(i, curr):
            if curr >= target:
                return curr == target

            if i >= len(nums):
                return False
            
            return func(i + 1, curr) or func(i + 1, curr + nums[i])
        
        return func(0, 0)