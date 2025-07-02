class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        minsum=0
        nums.sort(reverse=True)
        for i in range(1,len(nums),2):
            minsum+=nums[i]
        return minsum