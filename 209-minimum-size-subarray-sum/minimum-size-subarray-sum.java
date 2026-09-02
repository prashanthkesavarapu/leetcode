class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left=0;
        int wind=0;
        int min=Integer.MAX_VALUE;
        for(int i=0;i<nums.length;i++){
            wind+=nums[i];
            while(wind>=target){
                min=Math.min(min,i-left+1);
                wind-=nums[left];
                left+=1;
                
            }
        }
        if(min==Integer.MAX_VALUE){
            return 0;
        }else{
            return min;
        }
        
    }
}