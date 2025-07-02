class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        y=[]
        for i in board:
            if "R" in i:
                ri=i.index("R")
                x=i
                break
        y=[board[i][ri] for i in range(8)]
        
        xs=''.join([i for i in x if i in "BRp"])
        ys=''.join([i for i in y if i in "BRp"])
        print(xs,ys)
        r = xs.count("Rp")+xs.count("pR")+ys.count("Rp")+ys.count("pR")
        return r
