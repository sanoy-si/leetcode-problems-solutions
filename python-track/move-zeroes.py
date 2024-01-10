class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        place_holder = 0
        while place_holder < len(nums) and nums[place_holder] != 0:
            place_holder += 1

        seeker = place_holder + 1

        while seeker < len(nums):
            while seeker < len(nums) and nums[seeker] == 0:
                seeker += 1

            if seeker < len(nums):
                nums[seeker], nums[place_holder] = nums[place_holder], nums[seeker]
            seeker += 1
            place_holder += 1

            while place_holder < len(nums) and nums[place_holder] != 0:
                place_holder += 1
