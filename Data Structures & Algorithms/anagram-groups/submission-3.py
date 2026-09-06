class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # how can we check that a word is an anagram of another word? 
        # use a hasmap for each word and see if they equal each other
        # can we.... lets just use sorting 

        # create hashmap of sorted strings 
        groups = {}

        for word in strs:  
            sorted_word = "".join(sorted(word))
            
            if sorted_word not in groups: 
                groups[sorted_word] = []
            
            groups[sorted_word].append(word)

        return list(groups.values())