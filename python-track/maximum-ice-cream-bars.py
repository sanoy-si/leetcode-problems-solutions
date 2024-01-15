class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counter = Counter(costs)
        sorted_cost = []
        
        for i in range(1, int(1e5) + 1):
            sorted_cost += ([i] * counter[i])
        
        count = 0
        for cost in sorted_cost:
            coins -= cost
            if coins < 0:
                break

            count += 1  

        return count


        