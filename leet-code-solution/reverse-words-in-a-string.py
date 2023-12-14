class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        extra_space_remove = " ".join(s.split())

        def Convert(string):
            li = list(string.split(" "))
            return li

        # Driver code
        lst = Convert(extra_space_remove)
        invert = " ".join(lst[::-1])
        invert = invert.strip()

        return invert