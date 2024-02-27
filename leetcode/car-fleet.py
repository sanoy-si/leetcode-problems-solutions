class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair.sort()
        
        times = [(target - position)/speed for position, speed in pair]
        stack = []
        
        for time in times:
            while stack and stack[-1] <= time:
                stack.pop()

            stack.append(time)
        
        return len(stack)