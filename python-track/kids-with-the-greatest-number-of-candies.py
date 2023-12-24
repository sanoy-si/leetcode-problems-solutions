class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ma = max(candies)
        res = []
        for candie in candies:
            if candie + extraCandies >= ma:
                res.append(True)
            else:
                res.append(False)
        return res