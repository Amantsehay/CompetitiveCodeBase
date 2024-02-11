class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        left, right , n = 0, 0, len(nums)
        count = {}
        uniques = len(Counter(nums))
        print(uniques)
        unq = 0
        ans = 0
        for i in range(n):
            curr = nums[i]
            count[curr] = count.get(curr, 0) + 1
            
            if count[curr] == 1:
                unq += 1
            while unq == uniques:
                if count[nums[left]] == 1:
                    unq -= 1
                count[nums[left]] -= 1
                left += 1


            ans += left

        return ans
        