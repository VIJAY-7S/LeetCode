class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        pre = 1
        psum = 2

        for i in range(2,n):
            temp=psum
            psum+=pre
            pre = temp

        return psum

        
        