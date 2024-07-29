class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty_profit = list(zip(difficulty, profit))
        difficulty_profit.sort()
        difficulty.sort()
        max_profit = []
        
        for i in range(len(difficulty)):
            if max_profit:
                max_profit.append((difficulty_profit[i][0], max(max_profit[-1][1], difficulty_profit[i][1])))
            
            else:
                max_profit.append((difficulty_profit[i]))
        
        profit = 0
        for i in range(len(worker)):
            idx = bisect_right(difficulty, worker[i]) - 1
            if idx >= 0:
                profit += max_profit[idx][1]
            
        return profit





