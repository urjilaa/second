class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic={}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    dic[list1[i]] = i+j

        lst=[]
        for i,j in dic.items():
            if j == min(dic.values()):
                lst.append(i)
        return lst