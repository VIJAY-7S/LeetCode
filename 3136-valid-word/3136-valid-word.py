class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        if any(i not in "0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm" for i in word):
            return False

        if all(i not in "aeiouAEIOU" for i in word):
            return False

        if all(i not in "QWRTYPSDFGHJKLZXCVBNMqwrtysdfghjklzxcvbnm" for i in word):
            return False
        
        return True
