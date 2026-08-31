import java.util.HashMap;
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count=0;
        int current_sum=0;
        HashMap<Integer,Integer> map= new HashMap<>();
        for(int d:nums){
            current_sum+=d;
            if(current_sum==k){
                count+=1;
            }
            if(map.containsKey(current_sum-k)){
                count+=map.get(current_sum-k);
            }
            map.put(current_sum,map.getOrDefault(current_sum,0)+1);
        }
        return count;
    }
} 