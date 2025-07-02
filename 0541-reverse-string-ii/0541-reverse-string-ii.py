class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        sr=""
        for i in range(0,len(s),2*k):
            st=s[i:i+k]
            sr+=st[::-1]
            sr+=s[i+k:i+2*k]
        return sr
        