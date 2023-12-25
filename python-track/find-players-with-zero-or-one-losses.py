class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = defaultdict(int)
        players = set()
        for winner,loser in matches:
            losers[loser] += 1
            players.update([winner,loser])
        
        answer = [[],[]]
        for player in players:
            if player not in losers:
                answer[0].append(player)
            elif losers[player] == 1:
                answer[1].append(player)
        
        answer[0].sort()
        answer[1].sort()
        
        return answer

                
        
        
        