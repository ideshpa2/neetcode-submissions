class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_t = {}
        freq_s = {}

        for char in s: 
            if char in freq_s: 
                freq_s[char] += 1 
            else: 
                freq_s[char] = 1 

        for char in t: 
            if char in freq_t: 
                freq_t[char] += 1 
            else: 
                freq_t[char] = 1 


        return freq_s == freq_t

