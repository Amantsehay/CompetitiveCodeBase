class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        # this is like traversing the array in two twice

        stack = []
        ans = {}
        n = len(nums)
        for i in range(2 * n):
            num = nums[i % n]
            while stack and stack[-1][1] < num:
                val = stack[-1][1]
                ind = stack[-1][0]
                if ind not in ans:
                    ans[ind] = num

                stack.pop()
            stack.append([i % n, num])
        print(stack)
        answer = [-1] * n

        for ind in ans:
            answer[ind] = ans[ind]
        return answer
        
                
