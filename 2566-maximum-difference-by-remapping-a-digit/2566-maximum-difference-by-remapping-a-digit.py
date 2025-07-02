class Solution:
    def minMaxDifference(self, num: int) -> int:
        s=str(num)
        s1=s
        s2=s
        for i in s:
            if i!='9':
                s1 = s.replace(i,'9',s.count(i))
                break
        print(s1)

        for i in s:
            if i!='0':
                s2 = s.replace(i,'0',s.count(i))
                break
        print(s2)

        return(int(s1)-int(s2))