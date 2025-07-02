class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lst=[]

        j=0
        for i in range(len(nums)):
            if nums[i] not in lst:
                lst.append(nums[i])
                nums[j]=nums[i]
                j+=1

        return j
        

            


        