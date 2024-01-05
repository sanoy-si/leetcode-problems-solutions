class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) in visited:
                    continue
                visited.add((i,j))
                visited.add((j,i))
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
           row.reverse()
        