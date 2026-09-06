class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can subtract current val from the overall targer integer
        # then we can try and see if the value exists in the hashmap
        # if exists, we can return the indices of the two values
        
        hashmap = {}
        
        # store value → index
        for i in range(len(nums)):
                    value = nums[i]
                    hashmap[value] = i

        # Step 2: Loop again to find the complement
        for i in range(len(nums)):
            value = nums[i]
            search_val = target - value
            if search_val in hashmap and hashmap[search_val] != i:
                return [i, hashmap[search_val]]
