class Solution:
    def largestOddNumber(self, num: str) -> str:
        s=""
        for i in range(len(num),0,-1):
            if int(num[i-1])%2==1:
                return num[:i]
        return s
            

        