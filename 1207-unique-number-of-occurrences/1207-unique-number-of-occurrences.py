class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l=[arr.count(i) for i in set(arr)]
        if len(set(l))==len(l):
            return True
        else:
            return False
        