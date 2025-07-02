class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst1=s1.split()
        lst2=s2.split()
        lst3=lst1+lst2
        return [x for x in lst3 if lst3.count(x)==1]
        