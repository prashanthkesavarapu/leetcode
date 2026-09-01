class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        ArrayList<Integer> arr=new ArrayList<>();
        for(int i:nums2){
            arr.add(i);
        }
        ArrayList<Integer> res=new ArrayList<>();
        for(int i=0;i<nums1.length;i++){
            if(arr.contains(nums1[i])){
                res.add(nums1[i]);
                arr.remove(Integer.valueOf(nums1[i]));

            }
        }
        int[] sol=new int[res.size()];
        int j=0;
        for(int i:res){
            sol[j]=i;
            j+=1;
            
        }
        return sol;
    }
}