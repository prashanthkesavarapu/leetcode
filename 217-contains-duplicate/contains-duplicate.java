import java.util.HashMap;
import java.util.Map;
import java.util.*;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set= new HashSet<>();

        for(int c:nums){
            if(set.contains(c)){
                return true;
            }
            set.add(c);
        }
        return false;
        
    }
}