class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        nums += nums
        ones_count = nums.count(1)
        min_zeros = inf
        curr_zeros = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                curr_zeros += 1
            
            if right - left + 1 > ones_count:
                if nums[left] == 0:
                    curr_zeros -= 1
                left += 1
            
            if right - left + 1 == ones_count:
                min_zeros = min(min_zeros, curr_zeros)

        return min_zeros
