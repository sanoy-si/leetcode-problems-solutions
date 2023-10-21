class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        p=[0 for i in nums]
        for i in range(len(nums)):
            p[i]=p[i-1]+nums[i]
        return p