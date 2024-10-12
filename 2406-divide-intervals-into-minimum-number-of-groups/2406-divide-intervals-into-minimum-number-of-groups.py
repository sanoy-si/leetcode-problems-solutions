class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = int(1e6) + 1
        prefix_sum = [0 for _ in range(n)]
        for left, right in intervals:
            prefix_sum[left] += 1
            if right < 1e6:
                prefix_sum[right] -= 1
        
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + prefix_sum[i]
        
        return max(prefix_sum)