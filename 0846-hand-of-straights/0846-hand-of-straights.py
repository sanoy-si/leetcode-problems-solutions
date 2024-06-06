class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        hand.sort()
        for num in hand:
            while counter[num] > 0:
                for i in range(groupSize):
                    if counter[num + i] <= 0:
                        return False

                    else:    
                        counter[num + i] -= 1

        return True