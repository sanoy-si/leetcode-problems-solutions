class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers_dict = defaultdict(lambda: [0, 0])

        for answer in answers:
            if answers_dict[answer + 1][0] == answers_dict[answer + 1][1]:
                answers_dict[answer + 1][0] += answer + 1
            
            answers_dict[answer + 1][1] += 1
        
        
        return sum([value[0] for value in answers_dict.values()])


             