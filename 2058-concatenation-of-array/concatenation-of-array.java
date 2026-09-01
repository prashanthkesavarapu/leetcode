class Solution {
    public int[] getConcatenation(int[] nums) {
        int m=nums.length;
        int n=nums.length*2;
        int[] arr=new int[n];

        for(int i=0;i<nums.length;i++){
            arr[i]=nums[i];
        }
        int j=0;
        for(int i=m;i<n;i++){
            arr[i]=nums[j];
            j+=1;
        }
        return arr;
    }
}