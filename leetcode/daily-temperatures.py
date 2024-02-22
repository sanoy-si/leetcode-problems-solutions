class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pairs = defaultdict(int)
        stack = []

        for i,temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                val = stack.pop()
                pairs[val] = i - val

            stack.append(i)

        ans = [pairs[i] for i in range(len(temperatures))] 

        return ans