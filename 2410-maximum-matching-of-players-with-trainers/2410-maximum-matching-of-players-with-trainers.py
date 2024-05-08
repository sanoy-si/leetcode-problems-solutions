class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        answer = 0
        players.sort()
        trainers.sort()

        p1 = p2 = 0

        while p1 < len(players):
            while p2 < len(trainers) and players[p1] > trainers[p2]:
                p2 += 1
            
            if p2 < len(trainers):
                answer += 1
                p1 += 1
                p2 += 1
            
            else:
                break
        
        return answer