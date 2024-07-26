class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.distances = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customers:
            self.customers[id] = {}
        
        self.customers[id]["check_in"] = [stationName,t] 

    def checkOut(self, id: int, stationName: str, t: int) -> None: 
        check_in = self.customers[id]['check_in'] 
        print(check_in)    
        self.distances[f"{check_in[0]}:{stationName}"].append(t - check_in[1])
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        all_distances = self.distances[f"{startStation}:{endStation}"]
        return sum(all_distances)/len(all_distances)
        



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)