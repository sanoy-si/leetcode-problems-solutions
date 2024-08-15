class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = defaultdict(int)
        for bill in bills:
            notes[bill] += 1
            change = bill - 5

            note_10 = min(change // 10, notes[10])
            notes[10] -= note_10
            change -= note_10 * 10

            note_5 = min(change // 5, notes[5])
            notes[5] -= note_5
            change -= note_5 * 5
            

            if change:
                return False
        
        return True
            