class Solution {
    public int longestOnes(int[] nums, int k) {
        int left=0;
        int zeros=0;
        int max=0;

        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                zeros+=1;
            }
            while(zeros>k){
                if(nums[left]==0){
                    zeros-=1;
                }
                left+=1;
            }
            max=Math.max(max,i-left+1);
        }
        return max;
    }
}