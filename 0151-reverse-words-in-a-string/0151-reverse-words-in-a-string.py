class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        r = ' '.join(l[::-1])
        return r
        