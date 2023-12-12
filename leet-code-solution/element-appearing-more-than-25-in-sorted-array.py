class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        #twent5_per = len(arr)//4
        for i in range(len(arr)):
            print(arr[i])
            if arr[i] == arr[i +  len(arr)//4]:
                print(arr[i])
                return arr[i]
