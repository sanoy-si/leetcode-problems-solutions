class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        seeker = placeholder = 0

        while seeker < len(nums):
            while placeholder < len(nums) and nums[placeholder] != 0:
                placeholder += 1

            seeker = placeholder + 1
            while seeker < len(nums) and nums[seeker] == 0:
                seeker += 1
            
            if placeholder < len(nums) and seeker < len(nums):
                nums[placeholder], nums[seeker] = nums[seeker], nums[placeholder]
                placeholder += 1
                seeker += 1
            else:
                break
                
        return nums