class Solution {
    public int pivotIndex(int[] nums) {
        int total=0;
        for(int c:nums){
            total+=c;
        }
        int ps=0,ss=0;
        for(int i=0;i<nums.length;i++){
            ss=total-ps-nums[i];
            if (ss==ps){
                return i;
            }
            ps+=nums[i];
        }
        return -1;
    }
}