class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def nextgreat(n,arr):
            for k in arr:
                if k>n:
                    return k
            return -1
        lst=[]
        for i in nums1:
            ind=nums2.index(i)
            lst.append(nextgreat(i,nums2[ind+1:]))  
        return lst