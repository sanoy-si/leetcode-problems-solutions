class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        #if it is already sorted return 0
        if sorted(arr) == arr:
            return 0

        #remove a prefix
        right_sorted_count = 1
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                break
            
            right_sorted_count += 1
        
        answer = n - right_sorted_count

        #remove a suffix
        left_sorted_count = 1
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                break
            
            left_sorted_count += 1
        
        answer = min(answer, n - left_sorted_count)


        #remove a middle
        left_sorted, right_sorted = arr[:left_sorted_count], arr[-right_sorted_count:]
        for i, num in enumerate(left_sorted):
            idx = bisect_left(right_sorted, num)
            current_length = (i + 1) + (len(right_sorted) - idx)
            if 0 < idx < right_sorted_count and right_sorted[idx - 1] == num:
                current_length += 1

            answer = min(answer, n - current_length)

        return answer



