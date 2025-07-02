class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bn = bin(n)[2:]
        l=['0' if i=='1' else '1' for i in bn]
        return int(''.join(l),2)