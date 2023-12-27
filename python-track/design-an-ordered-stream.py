class OrderedStream:

    def __init__(self, n: int):
        self.dictionary = {}
        self.length = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.dictionary[idKey] = [value,0]
        chunk = []
        for key in range(idKey,self.length + 1):
            if key not in self.dictionary or (key != 1 and (key - 1 not in self.dictionary or not self.dictionary[key-1][1])):
                break
            chunk.append(self.dictionary[key][0])
            self.dictionary[key][1] = 1

        return chunk
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)