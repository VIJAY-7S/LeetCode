class Solution:
    def isHappy(self, n: int) -> bool:
        def square_of_digits(n):
            l=[(int(x)**2) for x in str(n)]
            return sum(l)
        
        loopnum=[]
        loop=False
        while not loop:
            r=square_of_digits(n)
            if r not in loopnum:
                loopnum.append(r)
                n=r
            else:
                loop=True
        if loopnum[-1]==1:
            return True
        else:
            return False