class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l1=heights.copy()
        l1.sort()
        c=0
        for i in range(len(l1)):
            if heights[i]!=l1[i]:
                c+=1
        return c
        