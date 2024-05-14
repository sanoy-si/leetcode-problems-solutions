class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        nums_set = set(nums)
        p = 0
        operations = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                p = max(p, nums[i] + 1)
                while p in nums_set:
                    p += 1
                
                operations += p - nums[i]
                p += 1

        return operations
