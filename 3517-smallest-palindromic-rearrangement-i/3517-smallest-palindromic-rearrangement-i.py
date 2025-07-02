class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s

        l1=list(s)
        l = len(l1)
        if l%2==0:
            s1=l1[:l//2]
            s1.sort()
            return ''.join(s1+s1[::-1])
        else:
            s1=l1[:l//2]
            s1.sort()
            return ''.join(s1+[s[l//2]]+s1[::-1])
            
        