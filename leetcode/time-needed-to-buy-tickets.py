class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque([[tickets[i], False if i != k else True] for i in range(len(tickets))])
        count = 0

        while True:
            front = q.popleft()

            if front[0]:
                count += 1
                q.append([front[0] - 1, front[1]])

            if front[1] and front[0] == 1:
                return count