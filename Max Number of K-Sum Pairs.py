class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c=0
        nums.sort()
        ln=len(nums)
        left=0
        right=ln-1
        while left<right:
            if nums[left]+nums[right]>k:
                right-=1
            elif nums[left]+nums[right]<k:
                left+=1
            else:
                c+=1
                left+=1
                right-=1
        return c
