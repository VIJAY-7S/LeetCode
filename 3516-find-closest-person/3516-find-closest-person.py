class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xd=abs(z-x)
        yd=abs(y-z)

        if xd==yd:
            return 0
        elif xd>yd:
            return 2
        else:
            return 1
        