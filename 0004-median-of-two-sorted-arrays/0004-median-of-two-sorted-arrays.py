class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nlst = nums1+nums2
        nlst.sort()
        l=len(nlst)
        if l%2==1:
            return nlst[l//2]
        else:
            return (nlst[l//2-1]+nlst[l//2])/2