class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sums = Counter([0])
        running_sum = 0
        ans = 0

        for num in nums:
            running_sum += num
            ans += sums[running_sum - goal]
            sums[running_sum] += 1
        
        return ans