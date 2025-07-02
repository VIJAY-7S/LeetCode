class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l= len(s)
        result = False
        for i in range(1,l):
            ss=s[:i]
            n=int((l/(i)))
            if ss*n==s:
                result = True
        return result