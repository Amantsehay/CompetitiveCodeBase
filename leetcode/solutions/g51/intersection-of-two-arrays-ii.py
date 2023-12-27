class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = [0] * 1002
        counter2 = [0] * 1002
        ans = []
        for i in range(len(nums1)):
            counter[nums1[i] + 1] += 1
        for i in range(len(nums2)):
            counter2[nums2[i] + 1] += 1
        print(counter)
        print(counter2)
        for i in range(1, 1002):
            ans.extend([i - 1] * (min(counter[i], counter2[i])))
        return ans

        
        
        