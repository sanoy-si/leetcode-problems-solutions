class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        squares.sort(key = lambda x: x[1])
        total = 0
        for x, y, l in squares:
            total += l ** 2

        n = len(squares)
        def check(y):
            current = 0
            for xi, yi, li in squares:
                removed = max(y - yi, 0)
                current += (max(0, li * (li - removed)))
            
            if abs(total / 2 - current) <= 10 ** -5:
                return 0

            elif total / 2 > current:
                return 1

            return -1 
        
        left = 1
        right = 10 ** 9
        answer = -1
        precision = 10 ** -6
        while right - left > precision:
            mid = (left + right) / 2
            result = check(mid)
            if result == 0:
                answer = mid
                right = mid - precision
            
            elif result == 1:
                right = mid - precision
                
            else:
                left = mid + precision

        return answer




                