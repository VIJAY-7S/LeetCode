class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=len(min([word1,word2],key = len))
        s=""
        for i in range(l):
            s+=(word1[i]+word2[i])
        s+=word1[l:]
        s+=word2[l:]
        return s
        