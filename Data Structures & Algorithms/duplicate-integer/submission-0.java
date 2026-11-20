class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer,Integer> numsMap = new HashMap<>();
        for(int i: nums){
            if(numsMap.containsKey(i)){
                return true;
            }
            numsMap.put(i,1);
        }
        return false;
    }
}