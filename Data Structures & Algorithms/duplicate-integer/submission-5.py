class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize set
        seen = set()

        # iterate thru array 
        for num in nums: 
            # check if in hashset
            if num in seen: 
                return True
            seen.add(num)

        return False


