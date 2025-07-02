class Solution:
    def countLargestGroup(self, n: int) -> int:
        lst1=[i for i in range(1,n+1)]
        lst2=[]
        for x in lst1:
            temp=list(str(x))
            temp=[int(y) for y in temp]
            lst2.append(sum(temp))
        print(lst1)
        print(lst2)
        maxf=max(lst2,key=lst2.count)
        maxc = lst2.count(maxf)
        c=0
        for i in set(lst2):
            if lst2.count(i)==maxc:
                c+=1
        return c