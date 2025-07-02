class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        result = False
        if s1==s2:
            result = True
        if len(s1)==len(s2):
            flag=2
            l=[]
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    l.append(i)
                    flag-=1
            if flag==0:
                s1=list(s1)
                s2=list(s2)
                c=s1[l[0]]
                s1[l[0]]=s1[l[1]]
                s1[l[1]]=c
                if s1==s2:
                    result = True
        return result
            
        