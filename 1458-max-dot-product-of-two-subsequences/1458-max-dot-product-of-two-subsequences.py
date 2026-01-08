class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = max(dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        
        if 0 not in nums1 and 0 not in nums2 and dp[n][m] == 0:
            return max(min(nums1) * max(nums2), max(nums1) * min(nums2))
        return dp[n][m]        