class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        lst1 = list(ransomNote)
        lst2 = list(magazine)
        flag=0

        for i in lst1:
            if lst1.count(i)<=lst2.count(i):
                flag+=1

        if len(lst1)==flag:
            return True
        else:
            return False
        