class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=""
        #num=num.split()

        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                ans=max(ans, num[i:i+3])
        return ans
       