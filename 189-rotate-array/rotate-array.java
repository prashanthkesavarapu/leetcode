class Solution {
    public void rotate(int[] nums, int k) {
        k=k%nums.length;
        int[] arr = new int[nums.length];
        int j=0;
        for(int i=nums.length-k;i<nums.length;i++){
            arr[j]=nums[i];
            j+=1;
        }
        int l=k;
        for(int i=0;i<nums.length-k;i++ ){
            
            arr[l]=nums[i];
            l++;
        }
        for(int i=0;i<nums.length;i++){
            nums[i]=arr[i];
        }
    }
}