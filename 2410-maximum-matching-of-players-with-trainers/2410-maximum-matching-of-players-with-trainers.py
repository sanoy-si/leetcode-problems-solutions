class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        cnt,p1,p2 = 0,0,0
        players.sort()
        trainers.sort()
        while p1 < len(players) and p2 < len(trainers):
            if players[p1] <= trainers[p2]:
                cnt += 1
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return cnt
                
        