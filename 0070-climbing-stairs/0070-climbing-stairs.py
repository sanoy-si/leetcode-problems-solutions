class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0

        def fucn(n):
            nonlocal count
            if n == 0:
                count += 1
                return 
            
            if n == 1:
                count += 1
                return
            
            fucn(n - 1)

            fucn(n - 2)
        
        fucn(n)

        return count
