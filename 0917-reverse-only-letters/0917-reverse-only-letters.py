class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s1=s[::-1]
        l1=[a for a in s1 if a.isalpha()]
        
        for ind,i in enumerate(s):
            if i.isalpha()==False:
                l1.insert(ind,i)

        return ''.join(l1)