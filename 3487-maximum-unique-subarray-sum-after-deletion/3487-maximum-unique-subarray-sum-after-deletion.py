class Solution:
    def maxSum(self, nums: List[int]) -> int:
        l1=list(set(nums))
        l1.sort(reverse=True)
        if l1[0]<0:
            return l1[0]
        elif l1[0]==0:
            return 0
        else:
            l2=[x for x in l1 if x>0]
            return sum(l2)
            
        
        
        