class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #vowels = "aeiou"
        #vowel_count = 0
        #i = 0
        #count = 0
        
        #for j in range(k, len(s), k):
        #    print(j)
        #    for i in range(j):
        #        if s[i] in vowels:
        #            count += 1
                #print(count)
        #    i += 1
        #    max_count = max(vowel_count, count)

        #return max_count

    ################################

        count = 0
        vowel_count = 0
        vowels = "aeiou"

        for i in range(len(s)):
            if s[i] in vowels:
                count += 1
            if i >= k and s[i-k] in vowels:
                count -= 1
            vowel_count = max(vowel_count, count)

        return vowel_count