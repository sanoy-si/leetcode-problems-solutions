class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        transpose = list(zip(*matrix))
        max_from_columns = [max(row) for row in transpose]
        
        answer = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if max_from_columns[j] == min(matrix[i]):
                    answer.append(max_from_columns[j])
                    break
        
        return answer
        
