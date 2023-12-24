class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ghost_min_disance = float('inf')
        for x,y in ghosts:
            curr = abs(x-target[0]) + abs(y - target[1])
            ghost_min_disance = min(ghost_min_disance,curr)
            
        pac_man_distance = abs(0-target[0]) + abs(0 - target[1])
        return pac_man_distance < ghost_min_disance 
            
            
        