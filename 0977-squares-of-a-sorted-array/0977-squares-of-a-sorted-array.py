class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l1=[i**2 for i in nums]
        l1.sort()
        return l1
        