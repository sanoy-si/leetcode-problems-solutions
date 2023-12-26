class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        _25 = floor(25 * len(arr) / 100)
        counter = Counter(arr)
        
        for key in counter:
            if counter[key] >_25:
                return key
        