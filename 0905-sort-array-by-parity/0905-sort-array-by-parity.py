from collections import deque
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        d=deque()
        for i in nums:
            if i%2==0:
                d.appendleft(i)
            else:
                d.append(i)
        return list(d)
        