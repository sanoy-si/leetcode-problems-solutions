class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = 0

        for i in range(len(nums)):
            if nums[i] <= target // 2:
                n = bisect_right(nums, target - nums[i]) - i - 1
                answer += (2 ** n) 
        
        return int(answer % int(1e9 + 7))