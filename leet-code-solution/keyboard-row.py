class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        result = []

        for i in words:
            word = i.lower()

            if len(set(first_row + word))==len(first_row) or len(set(second_row + word)) == len(second_row) or len(set(third_row + word)) == len(third_row):
                result.append(i)

        return result 