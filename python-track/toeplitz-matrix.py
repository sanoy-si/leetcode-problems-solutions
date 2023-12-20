class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        flag = True
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    flag = False
                    break
        
        return flag
        