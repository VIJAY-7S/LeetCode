class Solution:
    def reverseVowels(self, s: str) -> str:
        lst=[]
        for i in s:
            if i in "aeiouAEIOU":
                lst.append(i)

        lst.reverse()
        c=0
        s=list(s)
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                s[i]=lst[c]
                c+=1
        return ''.join(s)



        