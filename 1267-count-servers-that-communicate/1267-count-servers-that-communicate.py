class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        d=0
        t=0
        l=len(grid)
        for i in range(l):
            lst1=grid[i]
            if sum(lst1)==1:
                y=lst1.index(1)
                c=0
                for k in grid:
                    if k[y]==1:
                        c+=1
                if c==1:
                    d+=1

        for x in grid:
            for y in x:
                if y==1:
                    t+=1
        return t-d



        