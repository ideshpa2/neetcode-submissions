class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Create your hash map
        anagram_groups = {}
        
        # 2. Go through the array and sort each string correctly
        for word in strs:
            # Sort the characters of the individual word
            sorted_word = "".join(sorted(word))
            
            # 3. Group them in the hash map using the sorted word as the key
            if sorted_word not in anagram_groups:
                anagram_groups[sorted_word] = []
            
            # Append the original word to the group
            anagram_groups[sorted_word].append(word)
            
        # 4. Return the values of the hash map as a list of lists
        return list(anagram_groups.values())
