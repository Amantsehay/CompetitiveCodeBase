class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        the_str=""
        i=0
        index=0
        while i<len(s):
            if index<len(spaces):
                j=spaces[index]
            if j==i:
                the_str+=" "
                index+=1
            the_str+=s[i]
            i+=1
        return the_str
