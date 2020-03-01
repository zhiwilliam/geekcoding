class Solution {
    //sort and try to find any overlop
    public boolean canAttendMeetings(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return true;
        }
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]); // sort by starting time should be fine
        int lastEnd = Integer.MIN_VALUE;
        for (int[] interval : intervals) {
            if (interval[0] >= lastEnd) {
                lastEnd = interval[1];
            }else {
                return false;
            }
        }
        return true;
    }
}