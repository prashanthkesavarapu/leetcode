class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max=0;
        ArrayList<Character> arr=new ArrayList<>();
        for(char i:s.toCharArray()){
            while(arr.contains(i)){
                arr.remove(0);
            }
            arr.add(i);
            max=Math.max(max,arr.size());
        }
        return max;
    }
}