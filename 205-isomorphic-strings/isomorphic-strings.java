class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character,Character> map = new HashMap<>();
        HashSet<Character> sets=new HashSet<>();
        HashSet<Character> sett=new HashSet<>();
        HashSet<String> pairs=new HashSet<>();

        for(int i=0;i<s.length();i++){
            sets.add(s.charAt(i));
            sett.add(t.charAt(i));
            pairs.add(s.charAt(i) +","+ t.charAt(i));
        }
        int a=sets.size();
        int b=sett.size();
        int c=pairs.size();

        return a==c && b==c;





        
    }
}