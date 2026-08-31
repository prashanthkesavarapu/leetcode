import java.util.Arrays;
class Solution {
    public int[] runningSum(int[] nums) {
        int[] arr=new int[nums.length];
        int summ=0;
        int i=0;
        for(int c:nums){
            summ+=c;
            arr[i]+=summ;
            i+=1;
        }
        return arr;

    }
}