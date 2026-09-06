class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        Set<Integer> hashSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());

        if (nums.length > hashSet.size()) {
            return true; 
        }
        else { return false; }
        
    }  

}
