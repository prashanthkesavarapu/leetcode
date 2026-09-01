class Solution {
    public int maxArea(int[] height) {
        int max=0;
        int n=height.length;
        int left=0;
        int right=n-1;

        while(left<right){
            int h=Math.min(height[left],height[right]);
            int w=right-left;
            int area=h*w;
            max=Math.max(area,max);
            if(height[left]<height[right]){
                left+=1;
            }else{
                right-=1;
            }
        }
        return max;
        
    }
}