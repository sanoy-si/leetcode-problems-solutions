class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ptr = len(digits) - 1

        while ptr >= 0:
            digits[ptr] += carry
            if digits[ptr] > 9:
                carry = int(str(digits[ptr])[0])
                digits[ptr] = int(str(digits[ptr])[1])
                ptr -= 1
            else:
                carry = 0
                break

        if carry != 0:
            digits.insert(0,carry)

        return digits

        