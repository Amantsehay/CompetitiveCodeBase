class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0 #the left and the right pointers 
        r = 0
        max_length = 0
        while r < len(s):
            char = s[r]  #the current char
            if char in seen and seen[char] >= l:
                l = seen[char] + 1 # if the current char is already in the seen dict and its is greater than the left index update the left index by one
            else:
                max_length = max(max_length, r - l + 1)
            seen[char] = r #add every char index pair into the dict

            r+=1

        return max_length
            
            

            


            
        