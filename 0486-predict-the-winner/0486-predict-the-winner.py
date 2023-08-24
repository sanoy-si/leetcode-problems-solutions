class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def play(rem,score1,score2,turn):
            if not rem:return score1 >= score2
            
            choice1 = play(
                rem[1:],
                score1 + rem[0] if turn ==1 else score1,
                score2 + rem[0] if turn ==2 else score2,
                1 if turn ==2 else 2 )
            
            choice2 = play(
                rem[:-1],
                score1 + rem[-1] if turn ==1 else score1,
                score2 + rem[-1] if turn ==2 else score2,
                1 if turn ==2 else 2 )
            
            if turn ==1:return choice1 or choice2
            return choice1 and choice2
        return play(nums,0,0,1)
        