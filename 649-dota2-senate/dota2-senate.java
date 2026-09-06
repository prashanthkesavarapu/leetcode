class Solution {
    public String predictPartyVictory(String senate) {
        Queue<Integer> radient = new LinkedList<>();
        Queue<Integer> dire = new LinkedList<>();
        int n=senate.length();
        for(int i=0;i<n;i++){
            if(senate.charAt(i)=='R'){
                radient.offer(i);
            }
            if(senate.charAt(i)=='D'){
                dire.offer(i);
            }
        }
        while(!radient.isEmpty()  && !dire.isEmpty()){
            int rindex=radient.poll();
            int dindex=dire.poll();

            if(rindex<dindex){
                radient.offer(rindex+n);
            }
            if(rindex>dindex){
                dire.offer(dindex+n);
            }
        }
        return radient.isEmpty() ? "Dire" : "Radiant";
    }
}