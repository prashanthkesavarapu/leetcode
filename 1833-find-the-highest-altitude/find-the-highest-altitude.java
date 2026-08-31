import java.util.*;
class Solution {
    public int largestAltitude(int[] gain) {
        int n=gain.length+1;
        int[] arr=new int[n];
        arr[0]=0;
        for(int i=1;i<n;i++){
            arr[i]=arr[i-1]+gain[i-1];
        }
        int max=arr[0];
        for(int i=0;i<n;i++){
            if(arr[i]>max){
                max=arr[i];
            }
        }
        return max;
        }
        
}