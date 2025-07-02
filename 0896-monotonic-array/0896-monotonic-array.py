class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l1 = nums.copy()
        l1.sort()
        l2=l1[::-1]

        if nums==l1 or nums==l2:
            return True
        else:
            return False
        