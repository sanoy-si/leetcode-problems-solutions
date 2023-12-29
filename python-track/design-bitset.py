class Bitset:

    def __init__(self, size: int):
        self.bit_set = ['0'] * size
        self.ones = 0
        self.fliped = False

    def fix(self, idx: int) -> None:
        if self.fliped:
            if self.bit_set[idx] == '1':
                self.ones += 1
            self.bit_set[idx] = '0'
        else:
            if self.bit_set[idx] == '0':
                self.ones += 1
            self.bit_set[idx] = '1'

    def unfix(self, idx: int) -> None:
        if self.fliped:
            if self.bit_set[idx] == '0':
                self.ones -= 1
            self.bit_set[idx] = '1'
        else:
            if self.bit_set[idx] == '1':
                self.ones -= 1
            self.bit_set[idx] = '0'
    def flip(self) -> None:
        if not self.fliped:
            self.fliped = True
        else:
            self.fliped = False
        self.ones = len(self.bit_set) - self.ones

    def all(self) -> bool:
        if len(self.bit_set) - self.ones == 0:
            return True
        return False

    def one(self) -> bool:
        if self.ones > 0:
            return True
        return False
            

    def count(self) -> int:
        return self.ones


    def toString(self) -> str:
        if self.fliped:
            temp_bit_set = ['0' if bit == '1' else '1' for bit in self.bit_set]
            return ''.join(temp_bit_set)

        return ''.join(self.bit_set)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()