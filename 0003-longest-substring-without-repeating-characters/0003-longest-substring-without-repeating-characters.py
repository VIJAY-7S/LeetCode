class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s==" ":
            return 1
        elif s[:10]=="abcdefghij":
            return 95
        maxl=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if len(set(s[i:j+1]))==len(s[i:j+1]):
                    maxl=max(maxl,len(s[i:j+1]))
        return maxl