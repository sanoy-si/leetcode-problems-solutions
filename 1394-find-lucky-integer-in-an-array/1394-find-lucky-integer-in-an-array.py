class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        for num in sorted(arr, reverse = True):
            if num == counter[num]:
                return num
        
        return -1