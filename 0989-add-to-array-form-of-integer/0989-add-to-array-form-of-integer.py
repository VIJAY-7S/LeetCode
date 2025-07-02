import sys
sys.set_int_max_str_digits(10050)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n=''.join([str(i) for i in num])
        r=str(int(n)+k)
        return [int(x) for x in r]
        