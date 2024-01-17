class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        front_k = list(reversed(cardPoints[:k]))
        back_k = list(reversed(cardPoints[-k:]))
        possible = front_k + back_k

        point =  max_point = sum(possible[:k])
        left = 0
        for right in range(k, 2 * k):
            point += possible[right]
            
            point -= possible[left]
            left += 1
            
            max_point = max(point, max_point)

        return max_point

        