class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answer = 0
        counter = Counter(answers)
        for key, count in counter.items():
            colors_count = ceil(count / (key + 1))
            answer += colors_count * (key + 1)

        return answer 


             