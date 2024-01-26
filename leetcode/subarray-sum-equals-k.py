class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        accumulator = 0
        counter = Counter([0])
        ans = 0

        for num in nums:
            accumulator += num
            ans += counter[accumulator - k]
            counter[accumulator] += 1
        
        return ans
