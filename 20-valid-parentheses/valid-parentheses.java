class Solution {
    public boolean isValid(String s) {
    HashMap<Character,Character> map=new HashMap<>();
    Stack<Character> st=new Stack<>();
    map.put(']','[');
    map.put(')','(');
    map.put('}','{');
    for(char ch:s.toCharArray()){
        if(map.containsKey(ch)){
            if(!st.isEmpty() && map.get(ch)==st.peek()){
                st.pop();
            }
            else{
                return false;
                }
        }
        else{
            st.push(ch);
        }        
    }
    return st.isEmpty();

        
    }
}