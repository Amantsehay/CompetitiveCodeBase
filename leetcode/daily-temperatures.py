class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        answer = [0] * n 
        stack = []
        for i in range(n):
            currTemp = temp[i]
            if not stack:
                stack.append([i, currTemp])
            while stack and stack[-1][1] < currTemp:
                answer[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i, currTemp])
       
        return answer
                


        
        