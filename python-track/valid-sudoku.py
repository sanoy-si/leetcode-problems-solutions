class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def three_by_three():
            for k in range(0,9,3):
                s1, s2, s3 = set(), set(), set()
                p = k

                for i in range(p,p+3): 
                    for j in range(9):
                        if 0 <= j < 3:
                            if board[i][j] != '.' and board[i][j] in s1:
                                return False
                            s1.add(board[i][j])

                        if 3 <= j < 6:
                            if board[i][j] != '.' and board[i][j] in s2:
                                return False
                            s2.add(board[i][j])

                        if 6 <= j < 9:
                            if board[i][j] != '.' and board[i][j] in s3:
                                return False
                            s3.add(board[i][j])

            return True

        def rows():
            for row in board:
                if len(row) - row.count('.') + 1 != len(set(row)):
                    return False
            return True

        def transpose():
            transposed_board = [[0 for i in board[0]] for j in board]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    transposed_board[j][i] = board[i][j]
            
            return transposed_board

        def cols():
            for row in transpose():
                if len(row) - row.count('.') + 1 != len(set(row)):
                    return False
            return True

        return three_by_three() and rows() and cols()

        