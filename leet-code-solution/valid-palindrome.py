class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        num_letters = "abcdefghijklmnopqrstuvwxyz1234567890"

        while l <= r:
            if s[l] not in num_letters:
                l += 1
            elif s[r] not in num_letters:
                r -= 1
            elif s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True