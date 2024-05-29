class Solution:
    def getSum(self, a: int, b: int) -> int:
        total = a ^ b
        carry = (a & b) << 1

        while carry:
            temp_total = total
            total = total ^ carry
            carry = (temp_total & carry) << 1
        
        return total