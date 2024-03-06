class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def is_valid(capacity):
            count = 1
            current = 0

            for weight in weights:

                current = current + weight
                if current > capacity:
                    count += 1
                    current = weight

                if count > days:
                    return False
            
            return True
    
        left = max(weights)
        ans = right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            if is_valid(mid):
                ans = mid
                right = mid - 1

            else:
                left = mid + 1   

        return ans             

