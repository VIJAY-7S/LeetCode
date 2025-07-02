from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst1=[]
        for r in range(len(nums)+1):
            lst1.extend(combinations(nums,r))
        lst1=[list(sub) for sub in lst1]
        return lst1