class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * (n + 1)
        for first, last, seats in bookings:
            answer[first - 1] += seats
            answer[last] -= seats
        
        accumulator = 0
        for i in range(n):
            accumulator += answer[i]
            answer[i] = accumulator
        
        answer.pop()

        return answer
        