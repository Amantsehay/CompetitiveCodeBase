class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check if it's a start of a sequence

        the_set = set(nums)
        longest = 0
        for num in the_set:
            if not num - 1 in the_set:
                length = 0
                while (num + length) in the_set:
                    length += 1
                longest = max(longest, length)
        return longest 