class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1 = p2 = 0
        n = len(name)
        m = len(typed)

        while p1 < n:
            while p2 < m and name[p1] != typed[p2]:
                p2 += 1
            
            if p2 >= m:
                return False

            p1 += 1
            p2 += 1
            

        if p1 == n:
            while p1 == n and p2 < m and name[p1 - 1] == typed[p2]:
                p2 += 1
            
            return p2 == m

        return False

        