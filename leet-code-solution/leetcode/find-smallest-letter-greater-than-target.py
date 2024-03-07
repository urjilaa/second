class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)-1

        while left <= right:
            mid = (left+right)//2
            if ord(letters[mid]) > ord(target):
                right = mid - 1
            elif ord(letters[mid]) <= ord(target):
                left = mid + 1
                
        return letters[left] if left < len(letters) else letters[0] 
