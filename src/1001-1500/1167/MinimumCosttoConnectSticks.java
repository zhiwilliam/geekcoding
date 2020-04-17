
public class MinimumCosttoConnectSticks {
    public int connectSticks(int[] sticks) {
        Queue<Integer> queue = new PriorityQueue<>((a,b)->a-b);
        
        for(int i : sticks)
            queue.add(i);
        
        int minCost = 0;
        while(queue.size() > 1){
            int first = queue.poll();
            int second = queue.poll();
            
            int sum = first + second;
            minCost += sum;
            
            queue.offer(sum);
        }
        
        return minCost;
    }
}