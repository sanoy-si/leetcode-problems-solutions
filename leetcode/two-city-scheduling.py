class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = []
        b = []

        for cost in costs:
            if cost[0] <= cost[1]:
                a.append(cost)
            else:
                b.append(cost)
        
        if len(a) > len(b):
            a.sort(key = lambda x: -abs(x[0] - x[1]))
            while len(a) != len(b):
                b.append(a.pop())

        elif len(a) < len(b):
            b.sort(key = lambda x: -abs(x[0] - x[1]))
            while len(a) != len(b):
                a.append(b.pop())

        ans = 0
        for i in range(len(a)):
            ans += a[i][0]
            ans += b[i][1]
        
        return ans

            
        