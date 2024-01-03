class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        def transpose_strs():
            transpose = [['' for i in strs] for j in strs[0]]
            for i in range(len(strs)):
                for j in range(len(strs[0])):
                    transpose[j][i] = strs[i][j]

            return transpose
            
        transpose = transpose_strs()
        count = 0
        for row in transpose:
            if row != sorted(row):
                count += 1
        
        return count