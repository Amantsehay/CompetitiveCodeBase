class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        s = set(arr2)
        ans = []
        ls = []
        for num in arr2:
            ans.extend([num] * count[num])
        for num in arr1:
            if num not in s:
                ls.append(num)
        ls.sort()
        return ans + ls
        


            

        
        