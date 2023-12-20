class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 1
        ans = 0
        p = 0
        while p < len(nums):
            if  nums[p] == 0:
                p += 1
                continue
            while p < len(nums) - 1 and nums[p] == nums[p+1]:
                count += 1
                p += 1
            ans = max(ans,count)
            count = 1
            p += 1
        
        return ans
            
        