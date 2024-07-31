class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        books.sort(key = lambda x: x[1], reverse = True)
        print(books)
        total_height = 0
        curr_width = 0
        curr_max_height = 0

        for width, height in books:
            if curr_width + width <= shelfWidth:
                curr_width += width
                curr_max_height = max(curr_max_height, height)
            
            else:
                total_height += curr_max_height
                curr_width = width
                curr_max_height = height
        total_height += curr_max_height
        return total_height
        