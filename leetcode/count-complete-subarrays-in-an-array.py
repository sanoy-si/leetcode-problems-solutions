class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))
        window = Counter()
        left = 0

        count = 0
        for right in range(len(nums)):
            window[nums[right]] += 1

            while len(window) == n:
                count += len(nums) - right

                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    window.pop(nums[left])

                left += 1
        
        return count