class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        return list(bin(x^y)[2:]).count('1')
        
        
        