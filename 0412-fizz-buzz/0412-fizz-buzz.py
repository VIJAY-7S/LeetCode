class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        lst = []
        for i in range(n):
            if (i+1)%3==0 and (i+1)%5==0:
                lst.append("FizzBuzz")
            elif (i+1)%3==0:
                lst.append("Fizz")
            elif (i+1)%5==0:
                lst.append("Buzz")
            else:
                lst.append(str(i+1))

        return lst
        