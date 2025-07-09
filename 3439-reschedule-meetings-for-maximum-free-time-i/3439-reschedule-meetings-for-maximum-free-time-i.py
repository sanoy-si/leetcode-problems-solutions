class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) ->  int:
        left_bound = []
        left = 0
        start = 0
        cnt = 0
        busy_time = []
        curr_time = 0
        for right in range(len(startTime)):
            if cnt == k:
                start = endTime[left]
                curr_time -= endTime[left] - startTime[left]
                left += 1
                cnt -= 1

            cnt += 1
            left_bound.append(start)
            curr_time += endTime[right] - startTime[right]
            busy_time.append(curr_time)
            
        right_bound = [eventTime] 
        end = eventTime
        cnt = 0
        right = len(startTime) - 1
        for left in range(len(startTime) - 1, -1, -1):
            if cnt == k:
                right -= 1
                cnt -= 1
            cnt += 1

            if left < len(startTime) - 1:
                right_bound.append(startTime[left + 1])
            


        
        right_bound = right_bound[::-1]
        answer = -inf
        for i in range(len(startTime)):
            answer = max(answer, right_bound[i] - left_bound[i] - busy_time[i])

        return answer
