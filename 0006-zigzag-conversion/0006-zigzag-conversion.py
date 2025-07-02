class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l1=[]
        l=len(s)
        while len(l1)<l:
            for i in range(1,numRows+1):
                if len(l1)==l:
                    break
                l1.append(i)
            for j in range(numRows-1,1,-1):
                if len(l1)==l:
                    break
                l1.append(j)
        s1=list(s)
        c=0
        d={}
        for i in l1:
            if i not in d:
                d[i]=s1[c]
            else:
                d[i]=d[i]+s1[c]
            c+=1
        s2=""
        for key in d:
            s2+=d[key]
        return s2
        
        