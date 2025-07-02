class Solution:
    def countAndSay(self, n: int) -> str:
        s="1"
        def RLE(s):
            lst=[]
            c=1
            for i in range(1,len(s)):
                if s[i]==s[i-1]:
                    c+=1
                else:
                    lst.append(str(c))
                    lst.append(s[i-1])
                    c=1
            lst.append(str(c))
            lst.append(s[-1])
            return''.join(lst)
        
        for k in range(n-1):
            s=RLE(s)
        return s



        