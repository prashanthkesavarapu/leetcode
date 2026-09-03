class Solution {
    public int search(int[] nums, int target) {
        int[] arr=nums.clone();
        Arrays.sort(arr);
        int index=Arrays.binarySearch(arr,target);
        if(index<0){
            return -1;
        }
        for(int i=0;i<nums.length;i++){
            if(nums[i]==target){
                return i;
            }
        }
        return -1;
    }
}