class Solution {
    private int maxDepth = 0;
    private int flatSum = 0;
    public int depthSumInverse(List<NestedInteger> nestedList) {
        if (nestedList == null || nestedList.size() == 0) {
            return 0;
        }
        int topDownSum = dfs(nestedList, 1);
        return flatSum * (maxDepth + 1) - topDownSum;
    }

    private int dfs(List<NestedInteger> nestedList, int curLevel) {
        if (nestedList == null || nestedList.size() == 0) {
            return 0;
        }
        int sum = 0;
        maxDepth = Math.max(curLevel, maxDepth);
        for (NestedInteger each : nestedList) {
            if (each.isInteger()) {
                flatSum += each.getInteger();
                sum += each.getInteger() * curLevel;
            }else {
                sum += dfs(each.getList(), curLevel + 1);
            }
        }
        return sum;
    }
}