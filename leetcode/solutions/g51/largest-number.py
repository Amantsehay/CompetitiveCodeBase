class Solution:
    def largestNumber(self, nums: List[int]) -> str:
    
        nums = list(map(str, nums))
        self.sort(nums)
        if nums[0] == "0":
            return "0"
        return "".join(nums)




    def sort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):

                comp  = nums[j] + nums[j + 1] <  nums[j + 1] + nums[j]
                if comp:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        


    

    
        