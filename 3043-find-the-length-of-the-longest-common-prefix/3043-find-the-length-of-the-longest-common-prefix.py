class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_set = set()
        for value in arr1:
            while value and value not in prefix_set:
                prefix_set.add(value)
                value//=10

        answer =0
        for value in arr2:
            while value and value not in prefix_set:
                value//=10

            if value != 0:
                answer = max(answer,len(str(value)))
                
        return (answer) 