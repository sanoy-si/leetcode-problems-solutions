class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        sum = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            ans = max(ceil(sum/(i+1)), ans)

        return ans