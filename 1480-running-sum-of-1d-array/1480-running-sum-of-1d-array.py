class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst1 = []
        sum = 0
        for i in nums:
            sum+=i
            lst1.append(sum)

        return lst1
        