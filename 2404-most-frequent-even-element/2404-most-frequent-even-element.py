class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        n=-1
        count=0
        l1=[x for x in nums if x%2==0]
        l1.sort(reverse = True)
        for i in l1:
            if l1.count(i)>=count:
                count=l1.count(i)
                n=i
        return n