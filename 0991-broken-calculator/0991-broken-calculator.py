class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:

        def recursion(n):
            if n < startValue:
                return startValue - n

            if startValue == n:
                return 0
            
            if n % 2 == 0:
                return 1 + recursion(n / 2)
            
            return 2 + recursion((n + 1) / 2)
        
        return int(recursion(target))
        

