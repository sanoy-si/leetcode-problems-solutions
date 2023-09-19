class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for i in piles:
            heappush(heap,-i)
        for i in range(k):
            val = heappop(heap)
            heappush(heap,val//2)
        return -sum(heap)