class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        def find_ind(num):
            ind = -1

            left, right = 0, len(starts) - 1

            while left <= right:
                mid = (left + right) // 2

                if starts[mid][0] >= num:
                    ind = starts[mid][1]
                    right = mid - 1

                else:
                    left = mid + 1
            
            return ind


        starts = [[intervals[i][0], i] for i in range(len(intervals))]
        starts.sort()

        answer = []

        for interval in intervals:
            ind = find_ind(interval[1])

            if ind == len(intervals):
                answer.append(ind)
            
            else:
                answer.append(ind)
        
        return answer