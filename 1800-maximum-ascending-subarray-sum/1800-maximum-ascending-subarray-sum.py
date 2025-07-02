class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ssum=nums[0]
        maxsum=nums[0]
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                ssum+=nums[i+1]
                print(ssum)
            else:
                ssum=nums[i+1]
            maxsum=max([maxsum,ssum])

        return maxsum