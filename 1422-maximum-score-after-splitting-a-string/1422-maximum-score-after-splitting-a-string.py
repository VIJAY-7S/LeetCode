class Solution:
    def maxScore(self, s: str) -> int:
        lst=list(s)
        maxc = 0
        l=len(lst)
        
        for i in range(0,l-1):
            left=lst[0:i+1]
            right=lst[i+1:l]
            sum = left.count('0')+right.count('1')
            maxc=max(sum,maxc)

        return maxc
        