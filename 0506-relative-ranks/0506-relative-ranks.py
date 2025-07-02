class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d={}
        lst=[]
        score1=score.copy()
        score1.sort(reverse=True)
        
        for i in range(1,len(score1)+1):
            d[score1[i-1]]=i
        for j in score:
            lst.append(str(d[j]))
        
        if '1' in lst:
            lst[lst.index('1')]="Gold Medal"
        if '2' in lst:
            lst[lst.index('2')]="Silver Medal"
        if '3' in lst:
            lst[lst.index('3')]="Bronze Medal"
        return lst