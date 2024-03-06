class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def is_valid(num):
            hour = h
            for pile in piles:
                hour -= ceil(pile / num)
                if hour < 0:
                    return False
            
            return True
        
        answer = right

        while left <= right:
            mid = (left + right) // 2

            if is_valid(mid):
                answer = mid
                right = mid - 1
            
            else:
                left = mid + 1

        
        return answer

                