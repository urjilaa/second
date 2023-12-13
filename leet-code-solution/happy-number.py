class Solution:
    def isHappy(self, n: int) -> bool:

        for i in range(30):
            m = list(map(int, list(str(n))))
            ans = 0

            for i in m:
                i = int(i)
                ans += (i*i)
            if ans == 1:
                return True
            else:
                n = ans
            i += 1
           
        return False