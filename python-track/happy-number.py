class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate(num):
            sum = 0
            for digit in str(num):
                sum += int(digit) ** 2
            
            return sum

        visited = set()
        result = calculate(n)

        while 1:
            if result in visited:
                return False
           
            visited.add(result)
            
            if result == 1:
                return True
           
            result = calculate(result)


        