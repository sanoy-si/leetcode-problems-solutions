class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1] + nums[i])
        left = 0
        right = left + k - 1

        m = int(-1e4)
        print(prefix, right, left)
        while right < len(nums):
            a = (prefix[right] - prefix[left] + nums[left])
            m = max(m,a/k)
            left += 1
            right += 1
        
        return m

