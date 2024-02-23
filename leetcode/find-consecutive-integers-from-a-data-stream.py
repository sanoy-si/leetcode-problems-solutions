class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.elements = deque()
        self.count = 0

    def consec(self, num: int) -> bool:
        if len(self.elements) == self.k:
            if self.value == self.elements.popleft():
                self.count -= 1
       
        self.elements.append(num)
        if num == self.value: 
            self.count += 1

        return self.count == self.k



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)