class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(lambda: -1)
        stack = []
        ans = []

        for num in nums2:
            while stack and stack[-1] < num:
                d[stack.pop()] = num
            
            stack.append(num)
        
        for num in nums1:
            ans.append(d[num])
        
        return ans