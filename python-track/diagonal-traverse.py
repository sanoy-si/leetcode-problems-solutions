class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        visited = set()
        row = len(mat)
        col = len(mat[0])

        answer = []
        dirn = 0
        for i in range(row):
            for j in range(col):

                if (i,j) in visited:
                    continue

                rind,cind = i,j
                temp = []

                while rind < row and rind >= 0 and cind < col and cind >= 0 and (rind,cind) not in visited:
                    visited.add((rind, cind))
                    temp.append(mat[rind][cind])
                    rind += 1
                    cind -= 1
                
                if dirn:
                    answer += temp
                    dirn = 0
                else:
                    answer += temp[::-1]
                    dirn = 1

        return answer



        