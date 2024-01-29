class Solution:
    def maxScore(self, s):
        zeros, ones, max_score = 0, 0, float('-inf')
        for i in range(len(s)):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            
            if i != len(s) - 1:
                max_score = max(zeros - ones, max_score)
        
        return max_score + ones

