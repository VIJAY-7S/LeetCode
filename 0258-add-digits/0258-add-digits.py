class Solution:
    def addDigits(self, num: int) -> int:

        def onedigit(n):
            if len(str(n))==1:
                return n
            else:
                n=sum([int(x) for x in list(str(n))])
                return onedigit(n)

        return onedigit(num)

        