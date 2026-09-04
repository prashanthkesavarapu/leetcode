class Solution {
    public int calPoints(String[] operations) {

        Stack<Integer> st=new Stack<>();

        for(String c:operations){
            if(c.equals("C")){
                st.pop();
            }
            else if(c.equals("D")){
                st.push(st.peek()*2);
            }
            else if(c.equals("+")){
                int a=st.pop();
                int b=st.peek();
                st.push(a);
                st.push(a+b);
            }
            else{
                st.push(Integer.parseInt(c));
            }
        }
        int sum=0;
        while(!st.isEmpty()){
            sum+=st.pop();
        }
        return sum;
        
    }
}