class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
            
    def book(self, start: int, end: int) -> bool:
        pieces = [(max(start, s), min(end, e)) for s,e in self.bookings 
                    if start < e and end > s]
        if len(pieces) > 0 and max([len([1 for s,e in self.bookings 
                    if st < e and en > s]) for st, en in pieces]) > 1:  return False
        self.bookings.append((start, end))
        return True