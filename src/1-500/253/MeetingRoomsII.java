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