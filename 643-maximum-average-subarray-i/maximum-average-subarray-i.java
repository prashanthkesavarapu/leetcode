class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int wind=0;
        for(int i=0;i<k;i++){
            wind+=nums[i];
        }
        int max=wind;
        for(int i=k;i<nums.length;i++){
            wind=wind+nums[i]-nums[i-k];
            max=Math.max(max,wind);
        }
        return (double)max/k;
    }
}