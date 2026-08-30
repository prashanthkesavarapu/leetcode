import java.util.HashMap;
class Solution {
    public int subarraySum(int[] nums, int k) {
        int co=0;
        int cs=0;
        HashMap<Integer,Integer> map=new HashMap<>();

        for(int c:nums){
            cs+=c;
            if(cs==k){
                co+=1;
            }
            if(map.containsKey(cs-k)){
                co+=map.get(cs-k);
            }

            map.put(cs,map.getOrDefault(cs,0)+1);
        }
        return co;
    }
} 