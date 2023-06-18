class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ln=len(nums)
        left=0
        right=ln-1
        ma=0
        while left<right:
            ma=max(nums[left]+nums[right],ma)
            left+=1
            right-=1
        return ma
