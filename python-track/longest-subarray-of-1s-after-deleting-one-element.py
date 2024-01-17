class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        length = 0
        zero_count = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            length = max(length, (right - left + 1) - zero_count)
        
        return min(length, len(nums) - 1)
            
        