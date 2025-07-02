class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        lst = list(set(nums))
        lst.sort()
        l=len(lst)
        
        if l>2:
            return(lst[-3])
        else:
            return lst[-1]

        