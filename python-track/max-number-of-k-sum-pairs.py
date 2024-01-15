class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0

        while left < right:
            curr_sum = nums[left] + nums[right]

            if curr_sum == k:
                count += 1
                left += 1
                right -= 1
            elif curr_sum < k:
                left += 1
            else:
                right -= 1
        
        return count

        