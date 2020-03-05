# 1162. As Far from Land as Possible

Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

```python
Example 1:



Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:



Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1
```

# Analysis
BFS on each land
# Source Code
```java
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
```
