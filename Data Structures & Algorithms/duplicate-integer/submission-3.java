class Solution {
    public boolean hasDuplicate(int[] nums) {
        
    Set<Integer> numbers = new HashSet<>(); 

    for (int num : nums) {
        numbers.add(num); 
    }

    if (nums.length > numbers.size()) {return true; } 

    return false; 

    }  

}
