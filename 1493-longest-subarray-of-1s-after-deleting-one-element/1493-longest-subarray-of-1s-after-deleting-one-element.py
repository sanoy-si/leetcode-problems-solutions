class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        left = 0
        cnt = 0
        ans = 0 
        for right in range(len(nums)):
            while cnt > 1:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            if nums[right] == 0:
                cnt += 1
            if cnt <= 1:
                ans = max(right-left,ans)

        return ans

        