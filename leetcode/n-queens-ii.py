class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        self.cols = set()
        self.first_diagonals = set()
        self.second_diagonals = set()

        self.count = 0

        def func(path, row, num_queen):
            
            if num_queen == 0:
                self.count += 1
                return
        
            for j in range(n):
                if j in self.cols or row - j in self.first_diagonals or row + j in self.second_diagonals:
                    continue
                
                self.cols.add(j)
                self.first_diagonals.add(row - j)
                self.second_diagonals.add(row + j)
                
                path[row][j] = 'Q'
                func(copy.copy(path), row + 1, num_queen - 1)
                path[row][j] = '.'
                
                self.cols.remove(j)
                self.first_diagonals.remove(row - j)
                self.second_diagonals.remove(row + j)
        
        func([['.' for i in range(n)] for j in range(n)], 0, n)

        return self.count

            
     
