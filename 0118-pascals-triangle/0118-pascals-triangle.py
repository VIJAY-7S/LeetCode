class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[1],[1,1]]
        if numRows==1:
            return [[1]]
        if numRows==2:
            return lst
        def pascal(lst1):
            lst2=[]
            for i in range(len(lst1)-1):
                lst2.append(lst1[i]+lst1[i+1])
            lst2.append(1)
            lst2.insert(0,1)
            lst.append(lst2)
        
        for i in range(numRows-2):
            pascal(lst[-1])
        return lst


        