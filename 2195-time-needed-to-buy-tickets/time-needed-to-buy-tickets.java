class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        Queue<Integer> q=new LinkedList<>();
        for(int i=0;i<tickets.length;i++){
            q.offer(i);
        }
        int time=0;
        while(!q.isEmpty()){
        for(int i=0;i<tickets.length;i++)
        {
            i=q.poll();
            tickets[i]--;
            time++;
            if(tickets[i]==0)
            {
                if(i==k)
                return time;
            }
            else{
                q.offer(i);
            }
        }
        }
        return time;
    }
}