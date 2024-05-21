class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []

        def func(num, ind):

            if ind == len(nums):
                subset = [nums[i] for i in range(len(nums)) if num & 1 << i ]
                self.subsets.append(subset)
                return
            
            func(num, ind + 1)
            num |= 1 << ind
            func(num, ind + 1)
        
        func(0, 0)

        return self.subsets
        