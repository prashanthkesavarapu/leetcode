import java.util.HashMap;
import java.util.Map;
import java.util.*;
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> set = new HashSet<>();
        HashSet<Integer> result = new HashSet<>();

        for(int c:nums1){
            set.add(c);
        }
        for(int c:nums2){
            if(set.contains(c)){
                result.add(c);
            }
        }
        int[] ans=new int[result.size()];

        int i=0;
        for(int c:result){
            ans[i]=c;
            i++;
        }
        return ans;
    }
}