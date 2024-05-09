class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        answer = 0

        for i in range(k):
            answer += max(0, happiness[i] - i)
        
        return answer