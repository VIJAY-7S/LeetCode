class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=""
        for i in s:
            if i.isalnum():
                i=i.lower()
                str1+=i
        return str1==str1[::-1]