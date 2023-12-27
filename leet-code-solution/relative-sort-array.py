class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new_lst = []

        for i in arr2:
            while i in arr1:
                new_lst.append(i)
                arr1.remove(i)
                
        return(new_lst + sorted(arr1))

        