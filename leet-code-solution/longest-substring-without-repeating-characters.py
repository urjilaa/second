class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_set = set()
        max_len = 0
        holder = 0
        for seeker in range(len(s)):
            while s[seeker] in s_set:
                s_set.remove(s[holder])
                holder += 1

            s_set.add(s[seeker])
            max_len = max(max_len, seeker - holder + 1)
        return max_len
        
        #se = set(s)
        #se = "".join(se)
        #print(s)
        #count = 0
        
        #l = 0
        #r = len(se)
        #if se[l:r] not in s:
        #    l += 1
        #    se.remove(se[0])
        
        #if se[l:r] not in s:
        #    r -= 1
        #    se.pop()
        
        #for i in range(len(se)):
        #    if s[i] in se:
        #        count += 1
        #print(count)
        #return count
