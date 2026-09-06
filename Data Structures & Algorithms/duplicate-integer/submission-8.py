class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # frequency counter hashmap 
        # as soon as value appears return true 

        # if never then return false 

        freq = {}

        for num in nums: 
            if num in freq: 
                return True
            else: 
                freq[num] = 1 

        return False 