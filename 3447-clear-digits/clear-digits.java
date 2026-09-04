import java.util.Stack;
class Solution {
    public String clearDigits(String s) {
        Stack<Character> st=new Stack<>();

        for(char i:s.toCharArray()){
            if(Character.isDigit(i)){
                st.pop();
            }
            else{
                st.push(i);
            }
        }
        StringBuilder sb=new StringBuilder();
        for(char c:st){
            sb.append(c);
        }
        return sb.toString();
        
    }
}