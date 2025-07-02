class Solution:
    def check(self, nums: List[int]) -> bool:

        def checkinc(lst):
            result = all(lst[i]<=lst[i+1]for i in range(len(lst)-1))
            return result
        
        result=False
        for x in range(len(nums)):
            rnum = nums+nums[:x]
            del rnum[:x]
            if checkinc(rnum):
                return True
        return result


        