class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        nums = set(nums)

        def func(nums, permutation):
            if not nums:
                self.permutations.append(permutation[:])
                return
            
            new_nums = nums.copy()
            for num in nums:
                new_nums.remove(num)
                permutation.append(num)
                func(new_nums, permutation)

                new_nums.add(num)
                permutation.pop()
        
        func(nums, [])

        return self.permutations