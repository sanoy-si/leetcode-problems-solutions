class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(mid):
            count = 0
            for citation in citations:
                if citation >= mid:
                    count += 1
            
            return count >= mid
        
        left, right = 0, len(citations)
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                answer = mid
                left = mid + 1
            
            else:
                right = mid - 1
        
        return answer
