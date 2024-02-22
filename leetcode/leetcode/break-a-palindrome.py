class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        p = list(palindrome)  
        c = Counter(p) 
        for i in range(len(p)//2):
            if c['a']//2 != len(p)//2 and p[i] == 'a':
                i += 1
            elif c['a']//2 != len(p)//2 and p[i] != 'a':
                p[i] = 'a'
                break
            if c['a']//2 == len(p)//2:
                p[-1] = 'b'

        p1 = ""
        for i in p:
            p1 += i
        return p1