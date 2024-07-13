class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        answer = 0
        heap = []
        curr_sum = 0

        for efficiency, speed in sorted(list(zip(efficiency, speed)), reverse = True):
            heappush(heap, speed)
            curr_sum += speed
            
            if len(heap) > k:
                curr_sum -= heappop(heap)

            answer = max(answer, curr_sum * efficiency)

        return answer
