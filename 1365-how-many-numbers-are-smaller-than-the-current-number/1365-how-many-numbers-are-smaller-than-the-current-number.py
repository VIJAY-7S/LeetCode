class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst=[]
        nums1=nums.copy()
        nums1.sort()

        for i in nums:
            lst.append(len(nums[:nums1.index(i)]))
        
        return lst