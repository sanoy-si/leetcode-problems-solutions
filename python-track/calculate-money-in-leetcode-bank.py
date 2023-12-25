class Solution:
    def totalMoney(self, n: int) -> int:
        q = n // 7
        r = n % 7
        ans = 0
        for i in range(1,q+1):
            value = (7) * (i + 6 + i) / 2
            ans += value
        
        value = (r)*(q+1 + q+r)/2
        ans += value

        return int(ans)

        