class Solution {
    //BFS store all the land
    public int maxDistance(int[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    visited[i][j] = true;
                    queue.offer(new int[]{i, j});
                }
            }
        }

        int[][] dire = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int res = -1;
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            for (int[] dir : dire) {
                int x = cur[0] + dir[0];
                int y = cur[1] + dir[1];
                if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length && !visited[x][y]) {
                    visited[x][y] = true;
                    grid[x][y] =  grid[cur[0]][cur[1]] + 1;
                    res = Math.max(res, grid[x][y]);
                    queue.offer(new int[]{x, y});
                }
            }

        }

        return res == -1 ? res : res - 1;
    }
}