class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False

        target = total / 2 

        memory = {}
        def func(i, curr):
            if curr >= target:
                return curr == target

            if i >= len(nums):
                return False
            
            if (i, curr) not in memory:
                memory[(i, curr)] = func(i + 1, curr) or func(i + 1, curr + nums[i])

            return memory[(i, curr)]

        return func(0, 0)