class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        tTime = 0
        for i in tasks:
            tTime += i[1]
        temp = max(tasks,key = lambda x:x[0])[0]
        tTime = max(temp,tTime)
        enum = list(enumerate(tasks))
        enum.sort(key = lambda x:x[1][0])
        time = 1
        ptr = 0
        heap = []
        ans = []

        while ptr < len(tasks):
            print(time,tTime)
            while ptr < len(tasks) and enum[ptr][1][0] <= time:
                heappush(heap,(enum[ptr][1][1],enum[ptr][0]))
                ptr += 1
            if heap:
                val = heappop(heap)
                ans.append(val[1])
                time += tasks[val[1]][1]
            else:time = enum[ptr][1][0]

        while heap:
            ans.append(heappop(heap)[1])
        return ans




        