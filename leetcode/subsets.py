class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets = set()

        def func(subset, ind):
            self.subsets.add(tuple(subset[:]))

            if ind == len(nums):
                return
            
            func(subset[:], ind + 1)
            subset.append(nums[ind])
            func(subset[:], ind + 1)
        
        func([], 0)

        return self.subsets
        