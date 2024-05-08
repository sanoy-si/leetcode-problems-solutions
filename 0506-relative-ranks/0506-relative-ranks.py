class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_map = {val:idx for idx, val in enumerate(sorted(score, reverse = True))}

        answer = []
        for val in score:
            if score_map[val] == 0:
                answer.append("Gold Medal")
            
            elif score_map[val] == 1:
                answer.append("Silver Medal")

            elif score_map[val] == 2:
                answer.append("Bronze Medal")

            else:
                answer.append(str(score_map[val] + 1))

        return answer 
