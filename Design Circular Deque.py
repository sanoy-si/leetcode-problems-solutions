class MyCircularDeque:

    def __init__(self, k: int):
        self.queue=[]
        self.le=0
        self.k=k
        

    def insertFront(self, value: int) -> bool:
        if self.le<self.k:
            self.queue.insert(0,value)
            self.le+=1
            return 1
        return 0
        
        

    def insertLast(self, value: int) -> bool:
        if self.le<self.k:
            self.queue.append(value)
            self.le+=1
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.queue.pop(0)
            self.le-=1
            return True
        return False
        

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.queue.pop()
            self.le-=1
            return True
        return False
        

    def getFront(self) -> int:
        if not self.isEmpty():return self.queue[0]
        return -1
        

    def getRear(self) -> int:
        if not self.isEmpty():return self.queue[-1]
        return -1
        

    def isEmpty(self) -> bool:
        return self.queue==[]
        

    def isFull(self) -> bool:
        return self.le==self.k
        

