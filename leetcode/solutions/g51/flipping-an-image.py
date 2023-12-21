class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            curr = image[i]
            curr.reverse()
            for j in range(len(curr)):
                curr[j] = 1 - curr[j]
            image[i] = curr
        return image
