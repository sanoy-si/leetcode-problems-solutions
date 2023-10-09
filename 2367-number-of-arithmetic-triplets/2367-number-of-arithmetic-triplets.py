class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[k] - nums[j] == diff == nums[j] - nums[i] == diff:
                        cnt += 1
        return cnt
        