class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub_array_sums = []
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                sub_array_sums.append(curr_sum)
        
        sub_array_sums.sort()

        prefix_sum = [0]
        for num in sub_array_sums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        return prefix_sum[right] - prefix_sum[left - 1]

