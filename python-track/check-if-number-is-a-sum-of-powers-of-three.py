class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        m = 15
        ans = False
        while n > 0 and m >= 0:
            while m >= 0 and 3**m > n:
                m -= 1

            if m >= 0 and n > 0:
                n -= 3**m
                m -= 1
            if n == 0:
                ans = True
                break
            
        
        return ans
                
            
        