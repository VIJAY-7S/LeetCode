class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s=''.join(str(x) for x in nums)
        l=s.split('0')
        
        return len(max(l,key=len))
        