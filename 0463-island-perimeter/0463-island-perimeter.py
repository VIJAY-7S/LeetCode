import numpy as np
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        pm=0
        arr=np.array(grid)
        for row in range(len(arr)):
            for col in range(len(arr[0])):
                if arr[row,col]:
                    Left=arr[row,col-1:col]
                    Right=arr[row,col+1:col+2]
                    Top=arr[row-1:row,col]
                    Bottom=arr[row+1:row+2,col]
                    sum = Left.sum()+Right.sum()+Top.sum()+Bottom.sum()
                    pm+=(4-sum)
        return int(pm)