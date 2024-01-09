class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        for i in range(len(mat)):
            answer += mat[i][i]
        
        coordinate = [0,len(mat) - 1]
        while coordinate[0] < len(mat):
            answer += mat[coordinate[0]][coordinate[1]]
            coordinate[0] += 1
            coordinate[1] -= 1
        
        if len(mat) %2 == 0:
            return answer
            
        return answer - mat[len(mat)//2][len(mat)//2]