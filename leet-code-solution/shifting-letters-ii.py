class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0 for _ in range(n+1)]
        for l, r, k in shifts:
            if k == 1:
                arr[l] += 1
                arr[r+1] -= 1
            else:
                arr[l] -= 1
                arr[r+1] += 1
        
        res = []
        for i in range(n):
            if i != 0: 
                arr[i] += arr[i - 1]
            new_chr_ascii = (ord(s[i]) - ord("a") + arr[i]) % 26 + ord("a")
            res.append(chr(new_chr_ascii))
        return "".join(res)