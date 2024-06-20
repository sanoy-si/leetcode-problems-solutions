class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(mid):
            curr_basket = position[0]
            curr_idx = 0
            for _ in range(m - 1):
                next_idx = bisect_left(position, curr_basket + mid)
                if next_idx == len(position):
                    return False
                
                curr_idx = next_idx
                curr_basket = position[next_idx]
            
            return True

        left = 1
        right = int(1e9)
        answer = left
        position.sort()

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                answer = mid
                left = mid + 1
            
            else:
                right = mid - 1
        
        return answer