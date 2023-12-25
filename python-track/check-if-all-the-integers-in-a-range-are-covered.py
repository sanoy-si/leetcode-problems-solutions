class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()
        for r in ranges:
            covered.update(set(range(r[0],r[1]+1)))

        return set(range(left,right+1)) <= covered       