class Solution:
    def removeDuplicates(self,nums: list[int]) -> int:
        left = 0
        right = 1
        m = max (nums)
        while  1:
            while right < len(nums) and nums[left] >= nums[right]:right +=1
            if right < len(nums): nums[left + 1] , nums[right] = nums[right], nums[left + 1] 
            left += 1
            if right == len(nums):break
        return left 



