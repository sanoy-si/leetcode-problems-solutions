class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def is_valid(num):
            return len(citations) - bisect_left(citations, num) >= num
        
        low = 0
        high = len(citations)
        h_index = 0

        while low <= high:
            mid = (low + high) // 2

            if is_valid(mid):
                h_index = mid
                low = mid + 1

            else:
                high = mid - 1

        return h_index 