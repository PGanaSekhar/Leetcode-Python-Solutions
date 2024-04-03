class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        l=len(image)
        for i in range(l):
            for j in range(l):
                if image[i][j]==1:
                    image[i][j]=0
                else:
                    image[i][j]=1
        return [i[::-1] for i in image]
