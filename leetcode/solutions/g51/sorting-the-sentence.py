class Solution:
    def sortSentence(self, s: str) -> str:
        # d = {}
        splited = s.split()
        ls = [""] * len(splited)
        for w in splited:
            index = int(w[-1])
            ls[index - 1] = w[:len(w) - 1]
        return " ".join(ls)



        