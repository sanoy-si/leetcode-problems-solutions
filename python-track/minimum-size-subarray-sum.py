class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
       
        s = 0
        ans = len(nums)
       
        if sum(nums) < target:
            return 0

        while left <= right < len(nums):
            s+=nums[right]

            while s >= target:
                ans = min(ans,right-left+1)
                
                s -= nums[left]
                left += 1
            
            right+=1
            
        return ans

        
     