class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msum=float('-inf')
        csum=0
        for i in nums:
            csum+=i
            msum = max(msum,csum)
            if csum<0:
                csum=0
        return msum
        