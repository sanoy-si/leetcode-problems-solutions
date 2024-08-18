class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        set_ = set()
        count = 0
        while True:
            print(heap, set_)
            curr = heappop(heap)
            count += 1
            if count == n:
                return curr
            
            if curr * 2 not in set_:
                heappush(heap, curr * 2)
                set_.add(curr * 2)
            if curr * 3 not in set_:
                set_.add(curr * 3)
                heappush(heap, curr * 3)
            if curr * 5 not in set_:
                set_.add(curr * 5)
                heappush(heap, curr * 5)
        

