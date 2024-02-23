class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        move = 0
        while target != 1 and maxDoubles:
            if target % 2 == 1:
                move += 1
                target -= 1

            target //= 2
            maxDoubles -= 1
            move += 1
        
        move += target - 1

        return move
            