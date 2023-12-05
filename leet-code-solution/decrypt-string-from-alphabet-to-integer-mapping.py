class Solution:
    def freqAlphabets(self, s: str) -> str:
        new=[]
        ans = ""

        alphs = string.ascii_lowercase
        "abcdefghijklmnopqrstuvwxyz"
        i = 0

        for i in range(len(s)):
            if s[i] == "#":
                a = new.pop()
                b = new.pop()
                new.append(b + a)
            else:
                new.append(s[i])
        for i in new:
            ans += alphs[int(i)-1]
            
        return ans
        

            

