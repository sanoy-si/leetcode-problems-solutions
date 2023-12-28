class FrequencyTracker:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.frequency_of_frequency = defaultdict(int)
        
    def add(self, number: int) -> None:
        old_frequency = self.frequency[number]

        self.frequency[number] += 1
        new_frequency = self.frequency[number]

        self.update_frequency(old_frequency,new_frequency)

    def deleteOne(self, number: int) -> None:
        old_frequency = self.frequency[number]
        
        if self.frequency[number]:
            self.frequency[number] -= 1

        new_frequency = self.frequency[number]
        self.update_frequency(old_frequency,new_frequency)

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency_of_frequency[frequency]

    def update_frequency(self,old_frequency,new_frequency):
        if old_frequency in self.frequency_of_frequency:
            self.frequency_of_frequency[old_frequency] -= 1

        self.frequency_of_frequency[new_frequency] += 1
        



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)