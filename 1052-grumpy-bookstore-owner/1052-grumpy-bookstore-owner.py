class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_customer = sum([customers[i] for i in range(len(customers)) if grumpy[i] == 0])
        max_satisfied = 0
        left = 0

        for right in range(len(customers)):
            if grumpy[right] == 1:
                total_customer += customers[right]
            
            while right - left + 1 > minutes:
                if grumpy[left] == 1:
                    total_customer -= customers[left]
                
                left += 1
            
            max_satisfied = max(max_satisfied, total_customer)
        
        return max_satisfied


