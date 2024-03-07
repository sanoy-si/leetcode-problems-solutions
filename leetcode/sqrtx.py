class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        low, high = 1, x // 2

        answer = low

        while low <= high:
            mid = (low + high) // 2

            if mid ** 2 <= x:
                answer = mid
                low = mid + 1
            
            else:
                high = mid - 1
        
        return answer
