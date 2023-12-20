class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_score, one_count, zero_count =0, 0, 0
        for i in range(n):
            one_count += nums[i]
        ans = []
        for i in range(n):
            curr = zero_count + one_count
            if curr == max_score:
                ans.append(i)
            elif curr > max_score:
                ans = [i]
                max_score = curr
            if nums[i] == 1:
                one_count -= 1
            else:
                zero_count += 1
        if zero_count == max_score:
            ans.append(n)
        elif zero_count > max_score:
            ans = [n]
        return ans

            

        