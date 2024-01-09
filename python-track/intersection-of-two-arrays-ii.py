class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter_1 = Counter(nums1)
        counter_2 = Counter(nums2)
        intersection = set(nums1) & set(nums2)

        answer = []
        for num in intersection:
            answer += [num] * min(counter_1[num], counter_2[num])
        
        return answer
