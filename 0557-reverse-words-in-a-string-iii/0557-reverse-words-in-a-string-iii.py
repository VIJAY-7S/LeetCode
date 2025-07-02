class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(' ')
        l1=[w[::-1] for w in l]
        return ' '.join(l1)
        