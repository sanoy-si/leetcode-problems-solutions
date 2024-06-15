class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        pair = list(zip(capital, profits))
        pair.sort()

        p = 0
        while p < len(profits) and pair[p][0] <= w:
            heappush(heap, -pair[p][1])
            p += 1
        
        for i in range(k):
            if heap:
                w -= heappop(heap)

            while p < len(profits) and pair[p][0] <= w:
                heappush(heap, -pair[p][1])
                p += 1
        
        return w
            
