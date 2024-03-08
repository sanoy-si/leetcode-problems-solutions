class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]

        left, right = 0, len(values) - 1

        ind = -1
        
        while left <= right:
            mid = (left + right) // 2

            if values[mid][0] <= timestamp:
                ind = mid
                left = mid + 1
            
            else:
                right = mid - 1
            
        return values[ind][1] if ind != -1 else ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)