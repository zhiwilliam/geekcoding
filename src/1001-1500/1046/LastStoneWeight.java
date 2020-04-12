class Solution {
    public int lastStoneWeight(int[] stones) {
        
        Queue<Integer> queue = new PriorityQueue<>((a,b)->b-a);
        for(int i : stones)
            queue.offer(i);
        
        while(queue.size() > 1){
            queue.offer(queue.poll() - queue.poll());
        }
        
        return queue.poll();
        
    }
}