class Solution:
    def balancedString(self, s: str) -> int:
        charCount = Counter(s)
        left = 0
        requiredLen = len(s) // 4
        res = inf

        for right in range(len(s)):
            charCount[s[right]] -= 1
            while left < len(s) and charCount['W'] <= requiredLen and charCount['Q'] <= requiredLen and charCount['E'] <= requiredLen and charCount['R'] <= requiredLen:
                res = min(res, right - left + 1)
                charCount[s[left]] += 1
                left += 1
                
        return res