class Solution:
    def maxFreqSum(self, s: str) -> int:
        v={}
        c={}
        for i in s:
            if i not in v and i in "aeiou":
                v[i]=1
            elif i in "aeiou":
                v[i]+=1
            elif i not in c:
                c[i]=1
            else:
                c[i]+=1
        mc=max([c[i] for i in c]+[0])
        mv=max([v[i] for i in v]+[0])
        return mc+mv
        
        