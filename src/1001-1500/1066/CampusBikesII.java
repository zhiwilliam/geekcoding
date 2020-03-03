class Solution {
    private int ans = Integer.MAX_VALUE;
    // dfs with memo
    public int assignBikes(int[][] workers, int[][] bikes) {
        dfs(new boolean[bikes.length], bikes, workers, 0, 0);
        return ans;
    }

    private void dfs(boolean[] visited, int[][] bikes, int[][] workers, int curWorker, int dis) {
        if (curWorker >= workers.length) {
            ans = Math.min(ans, dis);
            return;
        }
        if (dis > ans) {
            return;
        }
        for (int i = 0; i < bikes.length; i++) {
            if (visited[i]) {
                continue;
            }
            visited[i] = true;
            dfs(visited, bikes, workers, curWorker + 1, dis + getDis(workers[curWorker], bikes[i]));
            visited[i] = false;
        }
    }

    private int getDis(int[] worker, int[] bike) {
        return Math.abs(worker[0] - bike[0]) + Math.abs(worker[1] - bike[1]);
    }
}