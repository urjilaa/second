class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        counter=Counter()
        l, r =0, 0
        ans=0
        for r in range(len(fruits)):
            counter[fruits[r]] +=1
            while len(counter) ==3:
                counter[fruits[l]] -=1
                if counter[fruits[l]] ==0:
                    del counter[fruits[l]]
                l +=1
            ans = max(ans, r-l+1)
        return ans
        