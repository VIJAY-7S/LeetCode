class Solution:
    def sumZero(self, n: int) -> List[int]:
        res=[i for i in range(-n//2+1,n//2+1)]
        
        if n%2==1:
            res=[i for i in range(-n//2+1,n//2+1)]
            return res
        elif n%2==0:
            res=[i for i in range(-n//2,n//2+1)]
            res.remove(0)
            return res

        