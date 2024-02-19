class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        path = path.split("/")
        print(path)
        n = len(path)
        for i in range(n):
            currChar = path[i]
            if currChar == "..":
                if len(stack) >=1:
                    stack.pop()
            elif currChar and currChar != ".":
                stack.append(currChar)
        
        return "/" + "/".join(stack)
