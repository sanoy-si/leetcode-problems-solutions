class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {j:i for i,j in enumerate(list1)}
        d2 = {j:i for i,j in enumerate(list2)}
        
        commons = set(list1) & set(list2)
        minimum = float(inf)
        for element in commons:
            minimum = min(minimum, d1[element] + d2[element])
        
        return [element for element in commons if d1[element] + d2[element] == minimum] 

        