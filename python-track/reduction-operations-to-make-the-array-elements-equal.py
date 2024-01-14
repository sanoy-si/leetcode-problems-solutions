class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        nums = list(sorted(set(nums), reverse = True))

        psum = []
        accumulator = 0

        for num in nums:
            accumulator += counter[num]
            psum.append(accumulator)
        
        return sum(psum[:-1])


        