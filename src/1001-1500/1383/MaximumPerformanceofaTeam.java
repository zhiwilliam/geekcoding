class Solution {
    //using priority queue
    //greey
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        int[][] matrix = new int[n][2];
        for (int i = 0; i < n; i++) {
            matrix[i][0] = efficiency[i];
            matrix[i][1] = speed[i];
        }
        Arrays.sort(matrix, (a, b) -> b[0] - a[0]);
        PriorityQueue<Integer> speedQueue = new PriorityQueue<>(k);
        long res = 0;
        long sumSpeed = 0;
        for (int[] entry : matrix) {
            sumSpeed += entry[1];
            speedQueue.offer(entry[1]);
            if (speedQueue.size() > k) {
                sumSpeed -= speedQueue.poll();
            }
            res = Math.max(res, (sumSpeed * entry[0]));

        }
        return (int) (res % (long)(1e9 + 7));
    }
}