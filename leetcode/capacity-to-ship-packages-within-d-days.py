class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def is_valid(capacity):
            day_count = 1
            current_total = 0

            for weight in weights:

                current_total = current_total + weight
                if current_total > capacity:
                    day_count += 1
                    current_total = weight

                if day_count > days:
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

