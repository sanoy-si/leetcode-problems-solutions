class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ln=len(nums)
        left=0
        right=ln-1
        nnums=[]
        while left<right:
            nnums.append(nums[right])
            nnums.append(nums[left])
            left+=1
            right-=1
        if left==right:nnums.append(nums[left])
        return nnums
