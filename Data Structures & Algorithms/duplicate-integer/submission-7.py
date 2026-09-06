class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize set
        seen = set()

        # iterate thru array 
        for _ in nums: 
            # check if in hashset
            if _ in seen: 
                return True
            seen.add(_)

        return False


