class Solution {
    public int largestAltitude(int[] gain) {
        int curr=0;
        int maxa=0;
        for(int c:gain){
            curr+=c;
            maxa=Math.max(curr,maxa);
        }
        return maxa;
        }
        
}