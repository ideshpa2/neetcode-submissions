class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can subtract current val from the overall targer integer
        # then we can try and see if the value exists in the hashmap
        # if exists, we can return the indices of the two values
        
        hashmap = {}
        
        # store value → index
        for index, value in enumerate(nums): 
            hashmap[value] = index

        # check for complement
        for index, value in enumerate(nums): 
            search_val = target - value
            if search_val in hashmap and hashmap[search_val] != index: 
                return [index, hashmap[search_val]]

            
