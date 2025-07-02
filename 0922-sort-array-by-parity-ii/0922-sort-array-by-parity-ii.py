class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l1=[i for i in nums if i%2==0]
        l2=[k for k in nums if k%2==1]

        for i in range(len(nums)):
            if i%2==0:
                nums[i]=l1[0]
                l1.pop(0)
            else:
                nums[i]=l2[0]
                l2.pop(0)
        return nums

        