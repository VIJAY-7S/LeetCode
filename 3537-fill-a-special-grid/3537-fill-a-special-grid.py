class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        def build(n, base):
            if n == 0:
                return [[base]]
                
            size = 2 ** (n - 1)
            total = size * size
            
            TR = build(n - 1, base)
            BR = build(n - 1, base + total)
            BL = build(n - 1, base + 2 * total)
            TL = build(n - 1, base + 3 * total)
                
            top = [tl_row + tr_row for tl_row, tr_row in zip(TL, TR)]
            bottom = [bl_row + br_row for bl_row, br_row in zip(BL, BR)]
                
            return top + bottom
        
        return build(N, 0)
