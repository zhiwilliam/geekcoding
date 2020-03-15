#1383. Maximum Performance of a Team

There are n engineers numbered from 1 to n and two arrays: speed and efficiency, where speed[i] and efficiency[i] represent the speed and efficiency for the i-th engineer respectively. Return the maximum performance of a team composed of at most k engineers, since the answer can be a huge number, return this modulo 10^9 + 7.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers. 

```python
Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
Example 2:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
Example 3:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
 

Constraints:

1 <= n <= 10^5
speed.length == n
efficiency.length == n
1 <= speed[i] <= 10^5
1 <= efficiency[i] <= 10^8
1 <= k <= n
```

#Analysis
Greedy problem can solve it using priority Queue:
sort the array by efficiency in descending order,
at the mean time store the speed in the priority queue, and if the queue size is larger than k,
we just poll out the min speed.
and update the total productivity by Math.max(curResult, totalSpeedSum * curEff);

#Source Code
```java
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
```