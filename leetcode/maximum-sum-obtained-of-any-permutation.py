class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq = [0] * (len(nums) + 1)
        for left, right in requests:
            freq[left] += 1
            freq[right + 1] -= 1
        
        accumulator = 0
        for i in range(len(freq)):
            accumulator += freq[i]
            freq[i] = accumulator
        
        freq.sort()
        nums.sort()

        ans = 0
        while nums:
            ans += (nums.pop() * freq.pop())
        
        return int(ans % (1e9 + 7))

       