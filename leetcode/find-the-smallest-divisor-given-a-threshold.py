class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def is_valid(divisor):
            total = 0

            for num in nums:
                total += ceil(num / divisor)

                if total > threshold:
                    return False
            
            return True


        low, high = 1, int(1e6)

        answer = high

        while low <= high:
            mid = (low + high) // 2

            if is_valid(mid):
                high = mid - 1
                answer = mid

            else:
                low = mid + 1

        return answer 