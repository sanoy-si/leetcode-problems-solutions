class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def find_max(arr):
            maximum = 0
            for i in range(3):
                for j in range(3):
                    maximum = max(maximum, arr[i][j])
            
            return maximum
        
        answer = []
        for i in range(len(grid) - 2):
            curr = []
            for j in range(len(grid) - 2):
                curr.append(find_max([[grid[l][k]  for k in range(j, j + 3)] for l in range(i, i + 3)]))
        
            answer.append(curr)
        
        return answer