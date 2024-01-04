class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf')
        smaller = float('inf')

        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= smaller:
                smaller = num
            elif num > smaller:
                return True

        return False 

        