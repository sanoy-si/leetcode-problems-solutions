class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.px_sum=[0]
        for i in nums:
            self.px_sum.append(self.px_sum[-1]+i)
    def sumRange(self, left: int, right: int) -> int:
        return self.px_sum[right+1]-self.px_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)