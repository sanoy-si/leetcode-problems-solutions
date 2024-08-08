class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dc = rc = 1
        lc = uc = 2
        pos = [rStart, cStart]
        curr_dir = 'r'
        is_valid = lambda pos: 0 <= pos[0] < rows and 0 <= pos[1] < cols
        answer = [pos[:]]
        
        while len(answer) < rows * cols:
            print(answer)
            if curr_dir == 'r':
                for _ in range(rc):
                    pos[1] += 1
                    if is_valid(pos):
                        answer.append(pos[:])
                rc += 2
                curr_dir = 'd'
            
            elif curr_dir == 'l':
                for _ in range(lc):
                    pos[1] -= 1
                    if is_valid(pos):
                        answer.append(pos[:])
                lc += 2
                curr_dir = 'u'
            
            elif curr_dir == 'd':
                for _ in range(dc):
                    pos[0] += 1
                    if is_valid(pos):
                        answer.append(pos[:])
                dc += 2
                curr_dir = 'l'
            
            else:
                for _ in range(uc):
                    pos[0] -= 1
                    if is_valid(pos):
                        answer.append(pos[:])
                    
                uc += 2
                curr_dir = 'r'
        
        return answer


