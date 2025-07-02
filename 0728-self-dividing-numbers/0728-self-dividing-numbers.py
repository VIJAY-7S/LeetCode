class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst1=[]
        for i in range(left,right+1):
            if '0' not in str(i):
                lst=[int(x) for x in str(i)]
                if all(i%x==0 for x in lst):
                    lst1.append(int(''.join([str(x) for x in lst])))
        return lst1

        
        