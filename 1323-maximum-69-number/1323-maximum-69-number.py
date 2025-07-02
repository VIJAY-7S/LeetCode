class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        if '6' in s:
            i6=s.index('6')
            result = '3' + (len(s)-1-i6)*'0'
            return int(result)+num
        return num
        
        