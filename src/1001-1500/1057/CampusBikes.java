class Solution {
    //sorting N * MLOG(MN) based on distance, suing priorityqueue
    //discussing have count sort approve, which need to work on too
    public int[] assignBikes(int[][] workers, int[][] bikes) {
        PriorityQueue<int[]> pair = new PriorityQueue<>((a, b) -> {
            if (a[0] == b[0]) {
                if (a[1] == b[1]) {
                    return a[2] - b[2];
                }
                return a[1] - b[1];
            }
            return a[0] - b[0];
        });
        for (int i = 0; i < workers.length; i++) {
            int[] worker = workers[i];
            for (int j = 0; j < bikes.length; j++) {
                int[] bike = bikes[j];
                int dist = Math.abs(worker[0] - bike[0]) + Math.abs(worker[1] - bike[1]);
                pair.add(new int[]{dist, i, j});
            }
        }

        int[] res = new int[workers.length];
        Set<Integer> bikeAssigned = new HashSet<>();
        Arrays.fill(res, - 1);
        while(bikeAssigned.size() < workers.length) {
            int[] cur = pair.poll();
            if (res[cur[1]] == -1 && bikeAssigned.add(cur[2])) {
                res[cur[1]] = cur[2];
            }
        }
        return res;
    }
}