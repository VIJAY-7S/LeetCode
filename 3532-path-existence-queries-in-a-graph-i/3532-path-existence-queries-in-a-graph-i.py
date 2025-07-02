class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n
        comp_id = 0
    
        for i in range(n):
            if i > 0 and nums[i] - nums[i-1] > maxDiff:
                comp_id += 1
            component[i] = comp_id
    
        answer = []
        for u, v in queries:
            answer.append(component[u] == component[v])
    
        return answer
        