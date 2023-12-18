from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.frequencyDict = defaultdict(int)
        self.frequencyDict2 = defaultdict(int)

    def add(self, number: int) -> None:
        old_frequency = self.frequencyDict[number]
        new_frequency = old_frequency + 1

        self.frequencyDict[number] = new_frequency
        self.frequencyDict2[old_frequency] -= 1
        self.frequencyDict2[new_frequency] += 1

    def deleteOne(self, number: int) -> None:
        if self.frequencyDict[number] > 0:
            old_frequency = self.frequencyDict[number]
            new_frequency = old_frequency - 1

            self.frequencyDict[number] = new_frequency
            self.frequencyDict2[old_frequency] -= 1
            self.frequencyDict2[new_frequency] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequencyDict2[frequency] >= 1

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
