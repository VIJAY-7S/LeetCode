class Solution:
    def countBits(self, n: int) -> List[int]:
        def dectobin(num):
            if num>=1:
                dectobin(num//2)
                lst.append(num%2)
                return lst
        
        ans=[0]
        for i in range(1,n+1):
            lst=[]
            l1=dectobin(i)
            ans.append(l1.count(1))
        return ans
        