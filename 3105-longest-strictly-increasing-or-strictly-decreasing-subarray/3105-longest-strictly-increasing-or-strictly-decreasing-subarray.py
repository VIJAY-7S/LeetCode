class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxc=1
        c=1
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                c+=1
            else:
                c=1
            maxc=max([maxc,c])
        c=1
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                c+=1
            else:
                c=1
            maxc=max([maxc,c])
        return maxc
        