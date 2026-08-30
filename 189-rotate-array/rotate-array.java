class Solution {
    public void rotate(int[] nums, int k) {
        k=k%nums.length;
        int n=nums.length;

        int[] x=new int[n];
        for(int i=0;i<k;i++){
            x[i]=nums[n-k+i];
        }
        for(int i=0;i<n-k;i++){
            x[k+i]=nums[i];
        }
        for(int i=0;i<n;i++){
            nums[i]=x[i];
        }
    }
}