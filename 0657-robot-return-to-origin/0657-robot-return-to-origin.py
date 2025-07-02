class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=moves.count('R')-moves.count('L')
        y=moves.count('U')-moves.count('D')
        
        if x==0 and y==0:
            return True
        else:
            return False
        