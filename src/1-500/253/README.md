# 253. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

```python
Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
```

# Analysis
Two pointer, one start pointer on start times and one end pointer on end times
or can sort based on end time and put all of them in the priority queue
# Source Code
```java
class Solution {
    //sort based by starting time, and keep a variable to update the end time
    public int minMeetingRooms(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        if (intervals.length == 1) {
            return 1;
        }
        int len = intervals.length;
        int[] startimes = new int[len];
        int[] endtimes = new int[len];
        for (int i = 0; i < len; i++) {
            startimes[i] = intervals[i][0];
            endtimes[i] = intervals[i][1];
        }
        Arrays.sort(startimes);
        Arrays.sort(endtimes);
        int startpointer = 0;
        int endpointer = 0;
        int usedRoom = 0;
        while(startpointer < len) {
            if (startimes[startpointer] >= endtimes[endpointer]) {
                usedRoom--;
                endpointer++;
            }
            usedRoom++;
            startpointer++;
        }
        return usedRoom;
    }
}
```