class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        ans = []
        for num in arr2:
            ans += [num] * counter[num]
        
        not_in_1 = list(sorted(list(set(arr1) - set(arr2))))
        for num in not_in_1:
            ans += [num] * counter[num]

        return ans

        