class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.dirns = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        self.visited = set()

        counter_board = Counter(sum(board, []))
        for char, count in Counter(word).items():
            if counter_board[char] < count:
                return False
            
        def in_bound(i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[0]) 

        def func(ind, i, j):
            if ind == len(word):
                return True

            if not in_bound(i, j) or word[ind] != board[i][j] or (i, j) in self.visited :
                return False

            self.visited.add((i, j))

            for dirn_i, dirn_j in self.dirns:
                if func(ind + 1, i + dirn_i, j + dirn_j):
                    return True
            
            self.visited.remove((i, j))

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if func(0, i, j):
                    return True
        
        return False