class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        d={}

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i+j not in d:
                    d[i+j] = [matrix[i][j]]
                else:
                    d[i+j].append(matrix[i][j])

        ans= []
        for ele in d.items():
            if ele[0] % 2 == 0:
                [ans.append(x) for x in ele[1][::-1]]
            else:
                [ans.append(x) for x in ele[1]]
        return ans