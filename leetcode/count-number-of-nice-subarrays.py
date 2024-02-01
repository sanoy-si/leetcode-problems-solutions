class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [num % 2 for num in nums]
        sums = Counter([0])

        running_sum = 0
        ans = 0
        for num in nums:
            running_sum += num
            ans += sums[running_sum - k]
            sums[running_sum] += 1
        
        return ans
