class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for num in nums:
            if not num % 2:
                even_sum += num
        ans = [0] * len(nums)
        index = 0
        for query in queries:
            i = query[1]
            curr_num = nums[i] + query[0]
            if not (nums[i] + query[0]) % 2:
                if nums[i] % 2:
                    even_sum += nums[i] + query[0]
                else:
                    even_sum += query[0]
            elif not nums[i] % 2:
                even_sum -= nums[i]
            nums[i] = curr_num
            ans[index] = even_sum
            index += 1
        return ans
        

            
        