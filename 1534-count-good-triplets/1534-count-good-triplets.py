class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        l1=len(arr)
        co=0
        for i in range(l1):
            for j in range(i+1,l1):
                for k in range(j+1,l1):
                    if (abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c):
                        co+=1
        return co