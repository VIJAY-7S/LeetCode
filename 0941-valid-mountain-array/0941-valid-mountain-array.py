class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxele = max(arr)
        def inc(subarr):
            return all([subarr[i]<subarr[i+1] for i in range(len(subarr)-1)])
        
        def dec(subarr):
            return all([subarr[i]>subarr[i+1] for i in range(len(subarr)-1)])

        if len(arr)<3:
            return False
        
        if inc(arr) or dec(arr):
            return False

        ind = arr.index(maxele)
        if inc(arr[:ind+1])==True and dec(arr[ind:]):
            return True