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

/**
 * The count sort solution is brilliantly.
 * Can just store all the pairs based on their distance
 * Just copied and paste from discussion
 */
class Solution {
    public int[] assignBikes(int[][] workers, int[][] bikes) {
        // Notice that the Manhattan distance is between 0 and 2000,
        // which means we can sort easily without even using priority queue
        int w = workers.length, b = bikes.length;
        int[] wo = new int[w], bi = new int[b];
        List<int[]>[] dists = new List[2001];
        Arrays.fill(wo, -1);
        Arrays.fill(bi, -1);
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < b; j++) {
                int[] worker = workers[i];
                int[] bike = bikes[j];
                int dist = Math.abs(worker[0] - bike[0]) + Math.abs(worker[1] - bike[1]);
                if (dists[dist] == null) {
                    dists[dist] = new ArrayList<int[]>();
                }
                dists[dist].add(new int[]{i, j});
            }
        }
        int assigned = 0;
        for (int i = 0; i <= 2000 && assigned < w; i++) {
            if (dists[i] == null) continue;
            for (int[] pair : dists[i]) {
                if (wo[pair[0]] == -1 && bi[pair[1]] == -1) {
                    wo[pair[0]] = pair[1];
                    bi[pair[1]] = pair[0];
                    assigned++;
                }
            }
        }
        return wo;
    }
}