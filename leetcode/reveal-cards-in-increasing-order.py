class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        answer = deque()
        deck.sort(reverse = True)

        for num in deck:
            if answer:
                answer.appendleft(answer.pop())
            
            answer.appendleft(num)

        return answer

