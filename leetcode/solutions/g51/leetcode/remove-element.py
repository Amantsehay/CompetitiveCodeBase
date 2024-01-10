class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

# class Solution(object):
#     def removeElement(self, list, val):
#         count = 0
#         for i in list:
#             if i == val:
#                 count += 1
#         for j in range(count):
#             list.remove(val)