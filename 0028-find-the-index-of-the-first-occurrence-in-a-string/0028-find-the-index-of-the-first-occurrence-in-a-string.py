class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle not in haystack:
            return -1
        else:
            l=len(needle)
            for i in range(len(haystack)):
                if haystack[i:i+l] == needle:
                    return i