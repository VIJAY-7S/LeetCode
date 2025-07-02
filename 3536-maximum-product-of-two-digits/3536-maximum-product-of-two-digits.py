class Solution:
    def maxProduct(self, n: int) -> int:
        lst = list(str(n))
        lst=[int(x) for x in lst]
        lst.sort()
        return lst[-1]*lst[-2]
        