class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.deque = deque()

    def enQueue(self, value: int) -> bool:
        if len(self.deque) == self.k:
            return False
        
        self.deque.appendleft(value)
        
        return True

    def deQueue(self) -> bool:
        if self.deque:
            self.deque.pop()
            return True
        
        return False

    def Front(self) -> int:
        return self.deque[-1] if self.deque else -1
        
    def Rear(self) -> int:
        return self.deque[0] if self.deque else -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return self.k == len(self.deque)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()