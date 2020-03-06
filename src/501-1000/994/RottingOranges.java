class Solution {
    public int orangesRotting(int[][] grid) {
        if (grid == null || grid.length == 0) {
            return -1;
        }
        int ans = -1;
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j});
                }
            }
        }
        if (queue.size() == 0) {
            for (int i = 0; i < grid.length; i++) {
                for (int j = 0; j < grid[0].length; j++) {
                    if (grid[i][j] == 1) {
                        return -1;
                    }
                }
            }
            return 0;
        }
        //starting BFS;
        int[][] directions = new int[][]{{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        while(!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cur = queue.poll();
                for (int[] dir : directions) {
                    int newRow = cur[0] + dir[0];
                    int newCol = cur[1] + dir[1];
                    if (validePosition(newRow, newCol, grid)) {
                        grid[newRow][newCol] = 2;
                        queue.offer(new int[]{newRow, newCol});
                    }
                }
            }
            ans++;
        }
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    return -1;
                }
            }
        }
        return ans;
    }

    private boolean validePosition(int row, int col, int[][] grid) {
        return row >= 0 && row < grid.length && col >= 0 && col < grid[0].length && grid[row][col] == 1;
    }
}