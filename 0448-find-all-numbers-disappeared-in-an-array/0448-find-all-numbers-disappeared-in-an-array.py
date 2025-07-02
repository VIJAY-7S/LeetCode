class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=len(nums)
        s1=set(range(1,l+1))
        s2=set(nums)
        return list(s1-s2)