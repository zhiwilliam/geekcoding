class Solution {
    //greedy and sort
    public int removeCoveredIntervals(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        Arrays.sort(intervals, (a, b) -> a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]);
        int end = 0;
        int prEnd = 0;
        int count = 0;
        for (int[] interval : intervals) {
            end = interval[1];
            if (prEnd < end) {
                count++; // only the last one can't cover the current, we add
                prEnd = end;
            }
        }
        return count;
    }
}