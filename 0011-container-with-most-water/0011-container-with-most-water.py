class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxvolume=0
        while right>left:
            w=right-left
            h=min(height[right],height[left])
            water=w*h
            print(w,h,water)
            maxvolume=max(maxvolume,water)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxvolume
                