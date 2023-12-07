class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        union_set = set()
        for a_range in ranges:
            union_set |= self.to_set(a_range[0], a_range[1])
        return union_set >= self.to_set(left, right) 

    def to_set(self, start, end):
        return {a for a in range(start, end + 1)}

        