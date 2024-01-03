class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = {heights[i]:names[i] for i in range(len(heights))}
        flag = False
        for i in range(len(heights)):
            for j in range(len(heights)-1):
                if heights[j] < heights[j+1]:
                    heights[j],heights[j+1] = heights[j+1],heights[j]
                    flag = True
            if not flag:
                break

        sorted_names=[data[height] for height in heights]
        return sorted_names
        

        