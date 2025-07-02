class Solution:
    def checkRecord(self, s: str) -> bool:
        result=False
        if s.count('A')<=1 and "LLL" not in s:
            result = True
        return result
        