class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        not_occupied = []
        occupied = []
        for i in range(n):
            heappush(not_occupied, i)

        idx_map = {i:times[i] for i in range(n)}
        times.sort()
        
        for i in range(n):
            arrival, leaving = times[i]
            while occupied and occupied[0][0] <= arrival:
                freed_seat = heappop(occupied)[1]
                heappush(not_occupied, freed_seat)
            
            smallest_free_seat = heappop(not_occupied)
            heappush(occupied, (leaving, smallest_free_seat))
            
            if idx_map[targetFriend] == times[i]:
                return smallest_free_seat
            