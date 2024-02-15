class Solution:
    def numberOfWays(self, s: str) -> int:
        z_cnt = 0
        o_cnt = 0
        z_prefix_sum = []
        o_prefix_sum = []

        for num in s:
            if num == '0':
                z_cnt += 1

            else:
                o_cnt += 1

            z_prefix_sum.append(z_cnt)
            o_prefix_sum.append(o_cnt)

        z_cnt = 0
        o_cnt = 0
        z_postfix_sum = []
        o_postfix_sum = []
        
        for num in s[::-1]:
            if num == '0':
                z_cnt += 1

            else:
                o_cnt += 1

            z_postfix_sum.append(z_cnt)
            o_postfix_sum.append(o_cnt)
        
        z_postfix_sum = z_postfix_sum[::-1]
        o_postfix_sum = o_postfix_sum[::-1]

        ans = 0

        for i,num in enumerate(s):
            if num == '0':
                ans += o_prefix_sum[i] * o_postfix_sum[i]
            else:
                ans += z_prefix_sum[i] * z_postfix_sum[i]

        return ans