import java.util.Arrays;
class Solution {
    public int[] runningSum(int[] nums) {
        int[] arr=new int[nums.length];
        int i=0;
        int s=0;
        for(int c:nums){
            s+=c;
            arr[i]=s;
            i+=1;
        }
        return arr;
    }
}