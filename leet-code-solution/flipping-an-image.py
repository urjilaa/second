class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for row in range(len(image)):
            image[row] = image[row][::-1]
            
        for row in range(len(image)):
            for col in range(len(image[0])):
                image[row][col] ^= 1
                print(row, col)   

        return image

                