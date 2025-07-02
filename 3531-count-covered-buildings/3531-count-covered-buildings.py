import bisect
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        from collections import defaultdict

        row_map = defaultdict(list)
        col_map = defaultdict(list)
        building_set = set()
    
        for x, y in buildings:
            row_map[x].append(y)
            col_map[y].append(x)
            building_set.add((x, y))
    
        for r in row_map:
            row_map[r].sort()
        for c in col_map:
            col_map[c].sort()
    
        count = 0
        for x, y in buildings:
            idx = bisect.bisect_left(row_map[x], y)
            left = idx > 0
            right = idx < len(row_map[x]) - 1
    
            idx = bisect.bisect_left(col_map[y], x)
            up = idx > 0
            down = idx < len(col_map[y]) - 1
    
            if left and right and up and down:
                count += 1
    
        return count
                    
        