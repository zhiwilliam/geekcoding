class Solution {
    //sort by the minimum saving
    public int twoCitySchedCost(int[][] costs) {
        if (costs == null || costs.length == 0) {
            return 0;
        }
        // a[0] - a[1] is the amount we save to go to A
        // sorted by most saved people
        Arrays.sort(costs, (a, b) -> (a[0] - a[1]) - (b[0] - b[1]));
        int len = costs.length / 2;
        int totalCost = 0;
        for (int i = 0 ; i < len; i++) {
            totalCost += costs[i][0] + costs[i + len][1];
        }
        return totalCost;
    }
}