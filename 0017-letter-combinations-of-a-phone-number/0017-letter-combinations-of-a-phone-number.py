class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        d={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        lst=list(d[digits[0]])

        def lc(digit,lst):
            lst1=[]
            for i in lst:
                for j in d[digit]:
                    lst1.append(i+j)
            return lst1
        
        for i in digits[1:]:
            lst=lc(i,lst)
        return lst
        

        