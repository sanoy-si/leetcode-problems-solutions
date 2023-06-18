class MinStack:
    stack=[]
    def __init__(self):
        self.stack=[]
        self.mins=[]
    def push(self, val: int) -> None:
        if self.mins:self.mins.append(min(self.mins[-1],val)) 
        else:self.mins.append(val)  
        self.stack.append(val)

    def pop(self) -> None:
        self.mins.pop()
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
