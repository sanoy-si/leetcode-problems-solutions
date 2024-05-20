class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def func(idx, curr_xor):
            nonlocal total
            if idx == len(nums):
                total += curr_xor
                return 

            func(idx + 1, curr_xor ^ nums[idx])
            func(idx + 1, curr_xor)
        
        func(0, 0)

        return total