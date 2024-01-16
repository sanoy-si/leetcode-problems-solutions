class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1 = p2 = 0
        while p1 < len(name) and p2 < len(typed) and name[p1] == typed[p2]:
            while p1 < len(name) and p2 < len(typed) and name[p1] == typed[p2]:
                p1 += 1
                p2 += 1
            while p2 < len(typed) and typed[p2] == typed[p2-1]:
                p2 += 1

        return p1 == len(name) and p2 == len(typed) 


        