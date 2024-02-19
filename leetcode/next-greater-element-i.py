class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        res = {}
        for num in nums2:
            if not stack:
                stack.append(num)
            while stack and stack[-1] < num:
                res[stack[-1]] = num
                stack.pop()
            stack.append(num)
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in res:
                ans.append(res[nums1[i]])
            else:
                ans.append(-1)
        return ans
                


        