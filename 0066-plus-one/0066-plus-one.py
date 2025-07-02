class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)
        num=0
        for i in range(l):
            d=digits[i]*(10**(l-i-1))
            num+=d  
        num+=1
        s=str(num)
        return([int(x) for x in s])
        