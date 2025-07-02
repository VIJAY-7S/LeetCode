class Solution:
    def reverse(self, x: int) -> int:
        v=0
        s=str(x)
        if s[0]=='-':
            v=int("-"+s[len(s):0:-1])
        else:
            v=int(s[::-1])

        if v>=(-2)**31 and v<=((2**31)-1):
            return v
        else:
            return 0
