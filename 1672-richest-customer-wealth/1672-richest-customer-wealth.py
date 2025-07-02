class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        r = sum(accounts[0])
        for i in accounts:
            s = sum(i)
            if s>r:
                r=s

        return r
        