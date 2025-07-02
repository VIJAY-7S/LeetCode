class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        l1=s.split('0')
        l2=s.split('1')

        m1=len(max(l1))
        m2=len(max(l2))

        if m1>m2:
            return True
        return False
        