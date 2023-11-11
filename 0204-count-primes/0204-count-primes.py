class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [0] * n
        cnt = 0
        sqt = sqrt(n)
        for i in range(2, n):
            if arr[i] == 0:
                cnt += 1
                if i <= sqt:
                    for j in range(i + i, n,  i):
                        arr[j] = 1
        
        return cnt

        