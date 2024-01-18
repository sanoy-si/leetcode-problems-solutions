class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_length = -1
        counter = Counter()
        left = 0
        for right in range(len(cards)):
            counter[cards[right]] += 1
            
            while right - left + 1 > len(counter):
                if min_length == -1 or min_length > right - left + 1:
                    min_length = right - left + 1
                    
                counter[cards[left]] -= 1
                if counter[cards[left]] == 0:
                    counter.pop(cards[left])
                
                left += 1
        
        return min_length
        