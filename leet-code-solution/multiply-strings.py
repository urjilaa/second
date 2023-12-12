class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
        r1 = 0
        r2 = 0
        
        for i in num1:
            r1=10*r1 + dic[i]
            print(r1)
        for j in num2:
            r2=10*r2 + dic[j]
            print(r2)
        return str(r1*r2)
            