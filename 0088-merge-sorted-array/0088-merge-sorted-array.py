class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.pop(-1)
        for i,ele in enumerate(nums1):
            if nums2 and ele>=nums2[0]:
                nums1.insert(i,nums2[0])
                nums2.pop(0)
        for i in nums2:
            nums1.append(i)