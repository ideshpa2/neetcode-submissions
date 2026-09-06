class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use meet in the middle pointers

        if len(s) != len(t): 
            return False

        freqs = {}
        freqt = {}

        for _ in s: 
            freqs[_] = freqs.get(_, 0) + 1
        
        for _ in t: 
            freqt[_] = freqt.get(_, 0) + 1
        
        return freqs == freqt

            