class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls_set = set()
        for r,c in walls:
            walls_set.add((r,c))
        
        guards_set = set()
        for r,c in guards:
            guards_set.add((r,c))
        
        guarded = set()
        
        for r,c in guards:
            tr = r - 1
            while tr >= 0 and (tr,c) not in walls_set and (tr,c) not in guards_set:
                guarded.add((tr,c))
                tr -= 1
            
            tr = r + 1
            while tr < m and (tr,c) not in walls_set and (tr,c) not in guards_set:
                guarded.add((tr,c))
                tr += 1
            
            tc = c - 1
            while tc >= 0 and (r,tc) not in walls_set and (r,tc) not in guards_set:
                guarded.add((r,tc))
                tc -= 1
            
            tc = c + 1
            while tc < n and (r,tc) not in walls_set and (r,tc) not in guards_set:
                guarded.add((r,tc))
                tc += 1
                
        count = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in guarded and (i,j) not in walls_set and (i,j) not in guards_set:
                    count += 1

        return count
                

            

        