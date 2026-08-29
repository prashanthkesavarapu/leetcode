import java.util.HashMap;
import java.util.Map;
import java.util.*;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer,Integer> map=new HashMap<>();

        for(int c:nums){
            map.put(c,map.getOrDefault(c,0)+1);
        }
        for(int x:map.keySet()){
            if(map.get(x)>1){
                return true;
            }
        }
        return false;

        
    }
}