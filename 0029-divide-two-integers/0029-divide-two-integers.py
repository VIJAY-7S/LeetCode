class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        r=int(dividend/divisor)
        if r<(-2)**31:
            r=(-2)**31
        elif r>2**31-1:
            r=2**31-1
        
        return r