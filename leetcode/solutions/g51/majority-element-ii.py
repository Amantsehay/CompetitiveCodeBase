class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_map = {}
        ans = []
        n = len(nums)
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
            if freq_map[num] > n // 3:
                ans.append(num)
                freq_map[num] = - 2 * n
        return ans

        