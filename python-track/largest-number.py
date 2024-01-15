class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        def compare(num1, num2):
            if num1 + num2 > num2 + num1:
                return 1
            return -1

        nums.sort(key = cmp_to_key(compare), reverse = True)
        
        return str(int(''.join(nums)))