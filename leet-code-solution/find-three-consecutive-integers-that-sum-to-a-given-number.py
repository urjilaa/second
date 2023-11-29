class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result=[]
        if num%3==0:
            n=num/3
            return n-1,n,n+1
        else:
            return []
        