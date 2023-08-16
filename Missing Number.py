class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums)
        snums = set(nums)
        for i in range(n + 1):
            if i not in snums:return i
        return n + 1
