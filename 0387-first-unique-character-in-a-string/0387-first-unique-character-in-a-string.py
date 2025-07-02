class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        result = -1
        for i in d:
            if d[i]==1:
                result = s.index(i)
                break
        
        return result