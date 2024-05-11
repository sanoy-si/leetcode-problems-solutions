class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        total_days = list(range(1, 366))
        days_set = set(days)
        memory = {}
        
        def dp(day):
            if day > 365:
                return 0

            if day not in days_set:
                return dp(day + 1)
            
            if day not in memory:
                memory[day] = min(costs[0] + dp(day + 1), costs[1] + dp(day + 7), costs[2] + dp(day + 30))

            return memory[day]
        
        return dp(1)