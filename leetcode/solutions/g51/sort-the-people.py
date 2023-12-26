class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            maxx = heights[i]
            k = i
            for j in range(i + 1, len(names)):
                if heights[j] > maxx:
                    maxx = heights[j]
                    k = j
            names[i], names[k] = names[k], names[i]
            heights[i], heights[k] = heights[k], heights[i]
        return names
                

        
        