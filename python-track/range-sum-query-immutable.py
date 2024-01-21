class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        accumulator = 0

        for num in nums:
            accumulator += num
            self.prefix_sum.append(accumulator)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
        
