class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dirn = 'East'
        self.pos = [0,0]
        self.num_to_circle =  2 * (self.width - 1) + 2 * (self.height - 1)
        

    def step(self, num: int) -> None:
        num %= self.num_to_circle
        while num != 0:
            if self.dirn == 'East':
                if self.pos[0] + 1 == self.width:
                    self.dirn = 'North'
                    continue
                self.pos[0] += 1
                num -= 1

            elif self.dirn == 'North':
                if self.pos[1] + 1 == self.height:
                        self.dirn = 'West'
                        continue
                self.pos[1] += 1
                num -= 1
            
            elif self.dirn == 'West':
                if self.pos[0] - 1 == -1:
                        self.dirn = 'South'
                        continue
                self.pos[0] -= 1
                num -= 1

            else:
                if self.pos[1] - 1 == -1:
                        self.dirn = 'East'
                        continue
                self.pos[1] -= 1
                num -= 1
        
        if self.pos == [0,0]:
            self.dirn = "South"
        elif self.pos == [self.width - 1,0]:
            self.dirn = "East"
        elif self.pos == [self.width - 1,self.height - 1]:
            self.dirn = "North"
        elif self.pos == [0,self.height - 1]:
            self.dirn = "West"

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dirn

        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()