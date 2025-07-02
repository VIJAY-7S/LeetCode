class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count=0
        for i in range(len(nums)):
            left = bisect_left(nums,lower-nums[i],i+1,len(nums))
            right = bisect_right(nums,upper-nums[i],i+1,len(nums))
            count+=(right-left)
        return count
        

        