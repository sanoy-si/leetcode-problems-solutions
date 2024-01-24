class NumArray:

    def __init__(self, nums: List[int]):
        running_sum = 0
        self.prefix_sum = [0]
        
        for num in nums:
            running_sum += num
            self.prefix_sum.append(running_sum)


    def sumRange(self, left: int, right: int) -> int:
       return self.prefix_sum[right + 1] - self.prefix_sum[left]
        
