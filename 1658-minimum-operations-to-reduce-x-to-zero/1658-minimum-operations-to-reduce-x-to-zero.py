class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = 0
        curr_sum = 0
        max_len = 0
        target = sum(nums) - x

        for right in range(len(nums)):
            curr_sum += nums[right]

            while left < right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len else -1