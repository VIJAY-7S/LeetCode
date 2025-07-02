class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l=[0,0]
        l[0]=list(set(nums1)-set(nums2))
        l[1]=list(set(nums2)-set(nums1))
        return l
        