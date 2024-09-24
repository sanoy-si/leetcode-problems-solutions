class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_length = 1
        operations = 0
        left = 0
        
        for right in range(1,len(nums)):
            operations += (nums[right] - nums[right - 1]) * (right - left)

            while operations > k:
                operations -= (nums[right] - nums[left])
                left += 1

            max_length = max(max_length, right - left + 1)
            
        return max_length