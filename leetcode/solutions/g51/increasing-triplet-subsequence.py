class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        largest = [float('-inf')] * (len(nums) + 1)
        smallest = [float('inf')] 
        n = len(nums)
        for i in range(1, n + 1):
            largest[n - i] = max(largest[n - i + 1], nums[n - i])
            smallest.append(min(smallest[-1], nums[i-1]))
        for i in range(n):
            if smallest[i] < nums[i] < largest [i]:
                return True
        return False


        