class Solution:
    def bestClosingTime(self, customers: str) -> int:
       customers = [1 if char == "Y" else -1 for char in customers]
       running_sum = 0

       max_sum = [0, 0]
       for i in range(len(customers)):
           running_sum += customers[i]

           if max_sum[0] < running_sum:
               max_sum = [running_sum, i + 1]

       return max_sum[1]