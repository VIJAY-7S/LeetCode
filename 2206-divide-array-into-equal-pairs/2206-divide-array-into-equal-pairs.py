class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(nums.count(x)%2==0 for x in set(nums))
        