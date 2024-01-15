class Solution:
    def characterReplacement(self, string, k):
        count = [0] * 128
        start = 0
        maxFrequency = 0
        maxLength = 0

        for end in range(len(string)):
            currentChar = string[end]
            count[ord(currentChar) - ord('A')] += 1
            maxFrequency = max(maxFrequency, count[ord(currentChar) - ord('A')])

            if end - start + 1 - maxFrequency > k:
                startChar = string[start]
                count[ord(startChar) - ord('A')] -= 1
                start += 1

            maxLength = max(maxLength, end - start + 1)

        return maxLength