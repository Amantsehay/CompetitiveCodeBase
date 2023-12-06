class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [a for pair in zip(nums[:n], nums[n:]) for a in pair]
