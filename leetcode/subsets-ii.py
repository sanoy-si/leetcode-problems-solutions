class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.subsets = set()

        def func(subset, ind):
            if ind == len(nums):
                self.subsets.add(tuple(sorted(subset)))
                return
            
            func(subset[:], ind + 1)
            subset.append(nums[ind])
            func(subset[:], ind + 1)
        
        func([], 0)

        return self.subsets

