class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # approach 
        # check by target for each number you are on then do a search 
        # in HASHMAP to see if that number even exists 

        index_map = {}

        for index, num in enumerate(nums):
            index_map[num] = index 

        for index, num in enumerate(nums): 
            looking_for = target - num 
            if looking_for in index_map and index_map[looking_for] != index: 
                return [index, index_map[looking_for]]

            