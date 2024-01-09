class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1,len(nums)):
            val = nums[i]
            p = i - 1
            while p >= 0 and nums[p] > val:
                nums[p+1] = nums[p]
                p -= 1

            nums[p + 1] = val
    
        