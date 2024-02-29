class Solution:
    def myPow(self, x: float, n: int) -> float:
        #return x**n
        #def pow(x, n):
        if n < 0:
            n = -(n) #change it to positive
            x = 1/x #invert the value

        if n == 0:
            return 1

        if n == 1:
            return x

        if n % 2 == 0:
            return self.myPow(x, n//2)**2
        else:
            return self.myPow(x, n//2)**2 * x
    
    