class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [i for i in range(len(s)) if s[i] == '|']

        answer = []


        for left, right in queries:
            if not candles:
                answer.append(0)
                continue

            left_most = min(bisect_left(candles, left), len(candles) - 1)
            right_most = max(bisect_right(candles, right) - 1, 0)
            
            if right >= candles[left_most] and left <= candles[right_most]:
                answer.append(candles[right_most] - candles[left_most] - (right_most - left_most)) 
            
            else:
                answer.append(0)
        
        return answer