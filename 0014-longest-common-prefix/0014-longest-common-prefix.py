class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sstr=strs[0]
        maxs=""
        for i in strs:
            if len(i)<len(sstr):
                sstr=i

        for j in range(len(sstr)):
            s=sstr[0:j+1]
            if all(s in st[0:j+1] for st in strs):
                maxs = sstr[0:j+1]
        return maxs

        