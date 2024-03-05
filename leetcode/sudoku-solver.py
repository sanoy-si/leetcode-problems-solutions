class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.rows = defaultdict(set)
        self.cols = defaultdict(set)
        self.squares = defaultdict(set)

        def next_index(i, j):
            if j < 8:
                return (i, j + 1)
            
            return (i + 1, 0)
            
        def is_valid(num, i, j):
            return num not in self.rows[i] and num not in self.cols[j] and num not in self.squares[get_square(i, j)]

                
        def get_square(i, j):
            if i < 3:
                if j < 3:
                    return 0

                if j < 6:
                    return 1
                
                return 2


            if i < 6:
                if j < 3:
                    return 3

                if j < 6:
                    return 4
                
                return 5

            
            if j < 3:
                return 6

            if j < 6:
                return 7
            
            return 8


        def func(i, j):
            if i == 9:
                return True
            
            next_i, next_j = next_index(i, j)
            if board[i][j] != '.':
                return func(next_i, next_j)

            for num in range(1, 10):
                num = str(num)
                if is_valid(num, i, j):

                    board[i][j] = num
                    self.rows[i].add(num)
                    self.cols[j].add(num)
                    self.squares[get_square(i, j)].add(num)

                    if func(next_i, next_j):
                        return True

                    board[i][j] = '.'
                    self.rows[i].remove(num)
                    self.cols[j].remove(num)
                    self.squares[get_square(i, j)].remove(num)
            
            return False
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    self.rows[i].add(board[i][j])
                    self.cols[j].add(board[i][j])
                    self.squares[get_square(i, j)].add(board[i][j])


        func(0, 0)