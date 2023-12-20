class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num - 3) % 3 == 0:
            num = (num - 3) // 3
            return [num,num+1,num+2]
        return []
        