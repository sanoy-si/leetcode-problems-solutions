# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def solve(x1,y1,x2,y2):
            if x1 > x2 or y1 > y2:
                return 0

            if not sea.hasShips(Point(x2,y2), Point(x1,y1)):
                return 0

            if x1 == x2 and y1 == y2:
                return 1 
                
            xm = (x1 + x2) // 2
            ym = (y1 + y2) // 2

            return solve(x1, y1, xm, ym) + solve(xm + 1, y1, x2, ym) + solve(x1, ym + 1, xm, y2) + solve(xm + 1, ym + 1, x2, y2)

        return solve(bottomLeft.x ,bottomLeft.y ,topRight.x, topRight.y)
        