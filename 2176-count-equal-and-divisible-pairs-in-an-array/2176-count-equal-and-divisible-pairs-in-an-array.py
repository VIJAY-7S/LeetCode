class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        l=len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i]==nums[j] and (i*j)%k==0:
                    count+=1
        return count
        