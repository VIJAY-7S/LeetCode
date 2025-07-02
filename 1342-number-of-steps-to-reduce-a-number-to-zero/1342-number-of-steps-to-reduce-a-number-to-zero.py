class Solution:
    def numberOfSteps(self, num: int) -> int:
        step=0
        for i in range(num):
            if num == 0:
                break
            elif num%2==0:
                num=num/2
            else:
                num = num-1
            step+=1
        return step
        