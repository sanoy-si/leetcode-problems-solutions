class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            if i > 0 and i < n - 1:
                dp[i][i] = nums[i - 1] * nums[i] * nums[ i + 1]
            elif i == 0:
                dp[i][i] = nums[i] * nums[i + 1]
            elif i == n - 1:
                dp[i][i] = nums[i] * nums[i - 1]
            else:
                dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                for k in range(left, right + 1):
                    if k == left:
                        inside_coins = dp[k + 1][right]
                    elif k == right:
                        inside_coins = dp[left][k - 1]
                    else:
                        inside_coins = dp[left][k - 1] + dp[k + 1][right]

                    left_val = nums[left - 1] if left - 1 >= 0 else 1
                    right_val = nums[right + 1] if right + 1 < n else 1
                    current_coins = left_val * nums[k] * right_val

                    dp[left][right] = max(dp[left][right], inside_coins + current_coins)
        

        return dp[0][n - 1]


        

                