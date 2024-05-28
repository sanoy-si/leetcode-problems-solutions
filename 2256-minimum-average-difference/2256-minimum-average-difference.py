class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [nums[0]]
        for num in nums[1:]:
            prefix.append(num + prefix[-1])
        
        suffix = [0]
        for i in range(n - 1, 0, -1):
            suffix.append(suffix[-1] + nums[i])
        suffix = suffix[::-1]

        min_avg_diff = inf
        min_avg_diff_idx = -1
        for i in range(n):
            first_avg = floor(prefix[i] / (i + 1))

            last_avg = 0
            if n - i - 1 > 0:
                last_avg = floor(suffix[i] / (n - i - 1))

            current_avg_diff = abs(first_avg - last_avg)
            if min_avg_diff > current_avg_diff:
                min_avg_diff = current_avg_diff
                min_avg_diff_idx = i
        
        return min_avg_diff_idx
        
