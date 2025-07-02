class Solution:
    def findComplement(self, num: int) -> int:
        bn= bin(num)[2:]
        l=[]
        for i in bn:
            if i=='0':
                l.append('1')
            else:
                l.append('0')

        s=''.join(l)
        return int(s,2)